import requests
import sys
from requests_toolbelt.multipart.encoder import MultipartEncoder

def submit_genome(genome_path, genome_name, ref_accnum=None):
    server = "https://www.pathogenomics.sfu.ca/islandviewer"
    ext = "/rest/submit/"

    fields = {
        "format_type": "GENBANK",
        'email_addr': 'anna.lewkowicz@student.kuleuven.be',
        'genome_name': genome_name,
        'genome_file': ('filename', open(genome_path, 'rb'), 'text/plain')
    }

    if ref_accnum:
        fields['ref_accnum'] = ref_accnum

    multipart_data = MultipartEncoder(fields=fields)
    headers={'Content-Type': multipart_data.content_type,
             'x-authtoken': 'MY_TOKEN'}

    r = requests.post(server+ext, headers=headers, data=multipart_data)
    
    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    print(repr(decoded))

if __name__ == "__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Usage: python islandviewer.py <path_to_genome_file> <genome_name> [ref_accnum]")
        sys.exit(1)

    genome_file_path = sys.argv[1]
    genome_name = sys.argv[2]
    ref_accnum = sys.argv[3] if len(sys.argv) == 4 else None
    submit_genome(genome_file_path, genome_name, ref_accnum)
