import glob, plistlib, sys, xml,requests
class VulnScanner(object):
    def __init__(self): self.url = 'https://vulmon.com/scannerapi?product={0}&version={1}&dev=1'
    def vulnerabilityCheck(self, product, version): return requests.get(self.url.format(product, version)).json()
def darwinSystemInfo():
    # this just iterates over /usr/local/Cellar/$app/$version
    brews = [x.split('/')[-2:] for x in glob.glob('/usr/local/Cellar/*/*')];apps = []
    for app in glob.glob("/Applications/*.app/Contents/Info.plist"):
        try:
            pl = plistlib.load(open(app, 'rb')); appname, appver = pl.get('CFBundleName', False), pl.get('CFBundleShortVersionString', False)
            if appname and appver: apps.append([pl['CFBundleName'], pl['CFBundleShortVersionString']])
            else: print('[!] Warning, error parsing {0}'.format(app), file=sys.stderr)
        except xml.parsers.expat.ExpatError as e: print('[!] Warning, error parsing {0}: {1}'.format(app, e), file=sys.stderr)
    return brews + apps
def main():
    scanner = VulnScanner()
    for app, ver in darwinSystemInfo():
        print(app, ver); print(scanner.vulnerabilityCheck(app, ver))
if __name__ == '__main__':
    main()
