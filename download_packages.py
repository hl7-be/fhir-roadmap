import urllib.request 
import shutil
import os

from AdvancedHTMLParser.Parser import AdvancedHTMLParser

serverlocation = 'https://build.fhir.org/ig/hl7-be/'
#igs = ['core','core-clinical','vaccination','allergy','lab']
igs = []
package = 'package.tgz'
target = './packages'
exclude = ['..','hl7-be-fhir-medication','hl7-be-fhir-laboratory-report','hl7-be-fhir-referral-prescription','hl7-be-patient-dossier']

os.makedirs(target, exist_ok=True)
urllib.request.urlretrieve(serverlocation, target +'/'+ 'index.html')
parser = AdvancedHTMLParser()
parser.parseFile(target +'/'+ 'index.html')
anchors = parser.getElementsByTagName('a') 
for anchor in anchors:
    igs.append( anchor.getAttribute('href').split('/')[0])

for ig in igs:
    if ig not in exclude:
        try:
            print(ig)
            urllib.request.urlretrieve(serverlocation +'/'+ig+'/'+package, target + '/'+ package)
            shutil.unpack_archive(target + '/'+ package, target + '/' + ig)
        except urllib.error.HTTPError:
            print('Package not published')    