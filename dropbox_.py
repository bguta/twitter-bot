"""
A module to read and write dropbox files and save them using dropbox
"""
import dropbox
import os

ac = ""  # add your own access key for dropbox api
dbx = dropbox.Dropbox(ac)


def upload(source, output, large=False):
    """
    @param source
    a file name e.g (test.txt). this is the file which is read

    @param output
    a file name for the output e.g (test.txt), this is the name
    as the file in dropbox
    """
    with open(source, "rb") as file:

        if not large:
            dbx.files_upload(file.read(),
                             "/" + output, mode=dropbox.files.WriteMode('overwrite'))
        else:
            with open(source, "rb") as f:

                # got this from ----> https://stackoverflow.com/a/43724479
                file_size = os.path.getsize(source)

                CHUNK_SIZE = 4 * 1024 * 1024

                upload_session_start_result = dbx.files_upload_session_start(
                    f.read(CHUNK_SIZE))

                cursor = dropbox.files.UploadSessionCursor(session_id=upload_session_start_result.session_id,
                                                           offset=f.tell())

                commit = dropbox.files.CommitInfo(path="/" + output,
                                                  mode=dropbox.files.WriteMode('overwrite'))

                while f.tell() < file_size:
                    if ((file_size - f.tell()) <= CHUNK_SIZE):
                        dbx.files_upload_session_finish(f.read(CHUNK_SIZE),
                                                        cursor,
                                                        commit)
                    else:
                        dbx.files_upload_session_append(f.read(CHUNK_SIZE),
                                                        cursor.session_id,
                                                        cursor.offset)
                        cursor.offset = f.tell()


def download(source, output):
    """
    @param source
    a file name e.g (test.txt). this is the file which is read in dropbox

    @param output
    a file name for the output e.g (test.txt), this is the name of the file
    to download
    """
    meta, res = dbx.files_download("/" + source)

    with open(output, "wb") as file:
        file.write(res.content)
