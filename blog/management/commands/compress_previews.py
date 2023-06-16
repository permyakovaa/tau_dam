from django.core.management.base import BaseCommand, CommandError
from ...models import File, Project, Event

import subprocess
import os

UPLOADS_DIR = 'uploads/'


class Command(BaseCommand):
    help = 'Generates compressed previews for new files'

    def add_arguments(self, parser):
        parser.add_argument('files_number', type=int)

    def handle(self, *args, **options):
        files_number = options['files_number']
        files = File.objects.filter(preview_compressed=False, compressing=False)[:files_number]

        self.compress_files(files)
        self.compress_thumbnails(Project.objects.filter(thumbnail_compressed=False)[:files_number])
        self.compress_thumbnails(Event.objects.filter(thumbnail_compressed=False)[:files_number])

        self.stdout.write(self.style.SUCCESS('Compress job finished'))
    
    def compress_files(self, items):
        for file in items:
            self.stdout.write(self.style.NOTICE(f'Reading file {UPLOADS_DIR}{file.file.name}'))
            file.compressing = True
            file.save()

            if file.is_video():
                self.generate_video_preview(file.file)
                self.compress_video(file.file)
            elif file.is_image():
                self.generate_image_preview(file.file)
            elif file.is_pdf():
                self.generate_pdf_preview(file.file)

            file.preview_compressed = True
            file.save()

        if len(items):
            self.stdout.write(self.style.SUCCESS('File previews generated'))

    def compress_thumbnails(self, items):
        for item in items:
            self.stdout.write(self.style.SUCCESS(f'Reading file {UPLOADS_DIR}{item.thumbnail.name}'))
            self.generate_image_preview(item.thumbnail)

            item.thumbnail_compressed = True
            item.save()

        if len(items):
            self.stdout.write(self.style.SUCCESS('Thumbnails generated'))

    def generate_video_preview(self, file):
        file_name = os.path.splitext(file.name)[0]
        subprocess.call([
            'ffmpeg', '-y', '-i', f'{UPLOADS_DIR}{file.name}', '-ss', '00:00:01.000', '-vframes', '1',
            '-q:v', '10', f'{UPLOADS_DIR}{file_name}_preview.jpg', '-hide_banner', '-loglevel', 'error'
        ])
        self.stdout.write(self.style.NOTICE(f'Generated file preview {UPLOADS_DIR}{file_name}_preview.jpg'))

    def compress_video(self, file):
        file_name = os.path.splitext(file.name)[0]
        file_extension = os.path.splitext(file.name)[1]
        subprocess.call([
            'ffmpeg', '-y', '-i', f'{UPLOADS_DIR}{file.name}', '-crf', '28',
            f'{UPLOADS_DIR}{file_name}_compressed{file_extension}', '-hide_banner', '-loglevel', 'error'
        ])
        self.stdout.write(self.style.NOTICE(
            f'Compressed video {UPLOADS_DIR}{file_name}_compressed{file_extension}'))

    def generate_image_preview(self, file):

        file_name = os.path.splitext(file.name)[0]
        file_extension = os.path.splitext(file.name)[1]
        subprocess.call([
            'ffmpeg', '-y', '-i', f'{UPLOADS_DIR}{file.name}', '-q:v', '30', '-vf',
            'scale=if(gte(a\,640/480)\,min(640\,iw)\,-2):if(gte(a\,640/480)\,-2\,min(480\,ih))',
            f'{UPLOADS_DIR}{file_name}_preview{file_extension}', '-hide_banner', '-loglevel', 'error'
        ])
        self.stdout.write(self.style.NOTICE(
            f'Generated file preview {UPLOADS_DIR}{file_name}_preview{file_extension}'))

    def generate_pdf_preview(self, file):
        file_name = os.path.splitext(file.name)[0]
        subprocess.call([
            'convert', '-resize', '10%', '-crop', '0x200+0+0',
            f'{UPLOADS_DIR}{file.name}[0]', f'{UPLOADS_DIR}{file_name}_preview.jpg'
        ])
        self.stdout.write(self.style.NOTICE(
            f'Generated file preview {UPLOADS_DIR}{file.name}'))