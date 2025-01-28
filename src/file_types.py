FILE_TYPES = {
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'bmp': 'Images',
    'tiff': 'Images',
    'webp': 'Images',
    'heif': 'Images',
    'ico': 'Images',
    
    'txt': 'TextFiles',
    'md': 'TextFiles',  # Markdown files
    'csv': 'TextFiles',  # Comma-separated values
    'log': 'TextFiles',  # Log files
    
    'pdf': 'Documents',
    'doc': 'Documents',  # Microsoft Word (Older)
    'docx': 'Documents',  # Microsoft Word (Modern)
    'ppt': 'Documents',  # PowerPoint files (Older)
    'pptx': 'Documents',  # PowerPoint files (Modern)
    'xls': 'Documents',  # Excel (Older)
    'xlsx': 'Documents',  # Excel (Modern)
    'odt': 'Documents',  # OpenDocument Text
    'rtf': 'Documents',  # Rich Text Format
    'epub': 'Documents',  # eBook format
    
    'mp3': 'Music',
    'wav': 'Music',
    'flac': 'Music',
    'aac': 'Music',
    'ogg': 'Music',
    'midi': 'Music',
    'alac': 'Music',  # Apple Lossless Audio Codec
    
    'mp4': 'Videos',
    'avi': 'Videos',
    'mov': 'Videos',
    'mkv': 'Videos',
    'webm': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
    '3gp': 'Videos',
    
    'exe': 'Executables',
    'bat': 'Executables',
    'sh': 'Executables',  # Shell scripts
    'app': 'Executables',  # MacOS Applications
    'dmg': 'Executables',  # MacOS Disk Images
    'pkg': 'Executables',  # MacOS package files
    
    'zip': 'Archives',
    'rar': 'Archives',
    'tar': 'Archives',
    'gz': 'Archives',
    '7z': 'Archives',
    'bz2': 'Archives',
    'xz': 'Archives',
    'iso': 'Archives',  # Disc Image files
    'tar.gz': 'Archives',
    'tgz': 'Archives',
    
    'html': 'WebFiles',
    'css': 'WebFiles',
    'js': 'WebFiles',
    'json': 'WebFiles',
    'xml': 'WebFiles',
    'php': 'WebFiles',
    'asp': 'WebFiles',
    
    'sqlite': 'Databases',
    'db': 'Databases',
    'sql': 'Databases',
    
    'apk': 'MobileApps',  # Android Apps
    'ipa': 'MobileApps',  # iOS Apps
    
    'psd': 'Graphics',  # Photoshop files
    'ai': 'Graphics',  # Adobe Illustrator files
    'eps': 'Graphics',  # Encapsulated PostScript
    'svg': 'Graphics',  # Scalable Vector Graphics
    'xd': 'Graphics',  # Adobe XD files
    'cdr': 'Graphics',  # CorelDraw files
}

TEMP_EXTENSIONS = [
    '.tmp',              # General temporary file extension
    '.crdownload',       # Google Chrome's temporary file extension during download
    '.part',             # Mozilla Firefox's partial download file extension
    '.download',         # Safari's temporary download file extension
    '.aria2',            # Aria2 download manager's temporary file extension
    '.swdownload',       # Microsoft Edge's temporary download extension
    '.xdownload',        # Internet Explorer's temporary download extension
    '.dmgpart',          # Partial download files used by macOS for disk image files
    '.ftl',              # File Transfer Protocol (FTP) partial file
    '.cfg',              # Configuration file that could be a temporary file
    '.wim',              # Windows Imaging Format temporary file
    '.iso.part',         # Partial ISO file (disk image) being downloaded
    '.~file',            # Temporary files created by some programs (e.g., LibreOffice, Microsoft Word)
    '.vdownload',        # Video download manager temporary file extension
    '.bak',              # Backup files (often created during a download or extraction process)
    '.ds_store',         # macOS system file created in directories (can appear as temp)
    '.tar.part',         # Partial TAR archive (tarball) during download
    '.zip.part',         # Partial ZIP archive during download
    '.gz.part',          # Partial GZIP archive during download
    '.bz2.part',         # Partial BZ2 archive during download
    '.mp3.part',         # Partial MP3 file during download
    '.avi.part',         # Partial AVI video file during download
    '.mov.part',         # Partial MOV video file during download
    '.flv.part',         # Partial FLV video file during download
    '.mkv.part',         # Partial MKV video file during download
    '.pdf.part',         # Partial PDF file during download
    '.txt.part',         # Partial text file during download
    '.xlsx.part',        # Partial Excel file during download
    '.docx.part',        # Partial Word document during download
    '.pptx.part',        # Partial PowerPoint file during download
    '.json.part',        # Partial JSON file during download
    '.xml.part',         # Partial XML file during download
    '.exe.part',         # Partial executable file during download
    '.tar.gz.part',      # Partial TAR.GZ archive during download
    '.rar.part',         # Partial RAR archive during download
    '.7z.part',          # Partial 7-Zip archive during download
    '.pkg.part',         # Partial macOS package file during download
    '.rpm.part',         # Partial RPM package file during download
    '.deb.part',         # Partial DEB package file during download
    '.apk.part',         # Partial APK file during download
    '.iso.part',         # Partial ISO file during download
    '.img.part',         # Partial IMG file during download
    '.zpart'             # Partial Z archive during download
]