from django.core.management.base import BaseCommand, CommandError
from ...models import File

import subprocess

UPLOADS_DIR = 'uploads/'


class Command(BaseCommand):
    help = 'Generates compressed previews for new files'

    def add_arguments(self, parser):
        parser.add_argument('files_number', type=int)

    def handle(self, *args, **options):
        files_number = options['files_number']

        files = File.objects.filter(preview_compressed=False, compressing = False)[:files_number]

        for file in files:
            self.stdout.write(self.style.SUCCESS('Reading file %s' % UPLOADS_DIR + file.file.name))
            file.compressing = True;
            file.save()

            if file.is_video():
                subprocess.call(
                    ['ffmpeg', '-y', '-i', UPLOADS_DIR + file.file.name, '-ss', '00:00:01.000', '-vframes', '1',
                     '-q:v', '10', UPLOADS_DIR + file.name() + '_preview.jpg', '-hide_banner', '-loglevel', 'error'])

                self.stdout.write(self.style.SUCCESS('Generated file preview "%s"' % UPLOADS_DIR + file.name() + '_preview.jpg'))

                subprocess.call(['ffmpeg', '-y', '-i', UPLOADS_DIR + file.file.name, '-crf', '28',
                                 UPLOADS_DIR + file.name() + '_compressed' + file.extension(), '-hide_banner', '-loglevel', 'error'])
                self.stdout.write(self.style.SUCCESS('Compressed video "%s"' % UPLOADS_DIR + file.name() + '_compressed' + file.extension()))
            elif file.is_image():
                subprocess.call(['ffmpeg', '-y', '-i', UPLOADS_DIR + file.file.name, '-q:v', '30', '-vf',
                                 'scale=if(gte(a\,320/240)\,min(320\,iw)\,-2):if(gte(a\,320/240)\,-2\,min(240\,ih))',
                                 UPLOADS_DIR + file.name() + '_preview' + file.extension(), '-hide_banner', '-loglevel', 'error'])

                self.stdout.write(self.style.SUCCESS('Generated file preview "%s"' % UPLOADS_DIR + file.name() + '_preview' + file.extension()))
            elif file.is_pdf():
                subprocess.call(['convert', '-resize', '10%', '-crop', '0x200+0+0', UPLOADS_DIR + file.file.name + '[0]', UPLOADS_DIR + file.name() + '_preview.jpg'])

                self.stdout.write(self.style.SUCCESS('Generated file preview "%s"' % UPLOADS_DIR + file.file.name + '[0]'))

            file.preview_compressed = True
            file.save()
        else:
            if len(files):
                self.stdout.write(self.style.SUCCESS('Successfully finished compress job'))
            else:
                self.stdout.write(self.style.WARNING('No files to compress'))

        return
