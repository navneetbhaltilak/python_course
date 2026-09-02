'''
🔄 File Copying
shutil.copyfileobj(fsrc, fdst[, length]) → Copy file-like object contents.

shutil.copyfile(src, dst) → Copy file contents only (no metadata).

shutil.copy(src, dst) → Copy file contents + permissions.

shutil.copy2(src, dst) → Copy file contents + metadata (timestamps).

📁 Directory Operations
shutil.copytree(src, dst) → Recursively copy entire directory tree.

shutil.rmtree(path) → Delete entire directory tree.

shutil.move(src, dst) → Move or rename files/directories.

📦 Archiving
shutil.make_archive(base_name, format, root_dir) → Create archive (ZIP, TAR, etc.).

shutil.unpack_archive(filename, extract_dir) → Extract archive contents.

shutil.get_archive_formats() → List supported archive formats.

shutil.register_archive_format(name, function, ...) → Register custom archive format.

shutil.unregister_archive_format(name) → Remove custom archive format.

⚙️ File Management Utilities
shutil.disk_usage(path) → Get disk usage stats (total, used, free).

shutil.chown(path, user=None, group=None) → Change file owner/group (Unix).

shutil.which(cmd) → Locate command in system PATH.

'''