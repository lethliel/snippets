import progressbar as pb

try:
    import urllib.request as urllib
except ImportError:
    import urllib
    
url = 'http://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso'
filename = 'tumbleweed.iso'

u = urllib.urlopen(url)

h = u.info()
totalSize = int(h["Content-Length"])
f = open(filename, 'wb')

blockSize = 8192
file_size_dl = 0
count = 0

num_bars = totalSize / blockSize


widgets = [filename + ': ', pb.Percentage(), ' ',  pb.Bar(), ' ', pb.ETA()]
bar = pb.ProgressBar(widgets=widgets, maxval=70).start()
already_done = 0


while True:
    chunk = u.read(blockSize)
    chunk_size = len(chunk)
    already_done += chunk_size
    done  = int(69 * already_done / totalSize)
    if not chunk: break
    f.write(chunk)
    bar.update(done)
f.close()


