#!/opt/bin/sh

python=/opt/bin/python3
script1=/opt/usr/src/examples-py/scripts/move-photo-files/move-photo-files.py
script2=/opt/usr/src/examples-py/scripts/move-photo-files/move-other-image-files.py

src_dir=/share/Multimedia/Camera\ Uploads
dest_dir=/share/Multimedia/Photo
log=/share/Multimedia/logs/move-photo-files.log

echo ${script1} -o "${dest_dir}" "${src_dir}"
${python} ${script1} -o "${dest_dir}" "${src_dir}" 2>&1 | tee -a ${log}

echo ${script2} -o "${dest_dir}" "${src_dir}"
${python} ${script2} -o "${dest_dir}" "${src_dir}" 2>&1 | tee -a ${log}
