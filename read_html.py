import os
import webbrowser
import tempfile
import requests


def read_html(page):
    """
    :param page:
        takes in text content or a "requests" response
    :return:
        1. creates a temporary html file
        2. renders that html file in a tab of your browser
        3. temp file is deleted
    """
    tmpdir = tempfile.mkdtemp()
    path = os.path.join(tmpdir, 'browse.html')
    file_path = 'file://' + path
    with open(path, "w") as f:
        if isinstance(page, requests.models.Response):
            f.write(page.text.encode('ascii', 'ignore'))
        elif isinstance(page, str):
            f.write(page.encode('ascii', 'ignore'))
        else:
            print "type not supported."
        f.close()
    print "Temporary file path: %s" % path
    return webbrowser.open(file_path)

if __name__ == '__main__':
    html = '<h1>Read HTML</h1>\n<p>The read_html function renders raw html in your browser.</p>'
    read_html(html)