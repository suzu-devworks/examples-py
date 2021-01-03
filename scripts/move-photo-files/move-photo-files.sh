#!/opt/bin/sh

python=/opt/bin/python3
script=/opt/usr/src/examples-py/scripts/move-photo-files/move-photo-files.py
src_dir=/share/Multimedia/Camera\ Uploads
dest_dir=/share/Multimedia/Photo
log=/share/Multimedia/logs/move-photo-files.log

echo ${python} ${script} -o "${dest_dir}" "${src_dir}"
${python} ${script} -o "${dest_dir}" "${src_dir}" 2>&1 | tee -a ${log}
