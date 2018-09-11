#!env python3

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"splunk.mysite.com"),
    ])).add_extension(
        x509.SubjectAlternateName([
            x509.DNSName(u"splunk.mysite.com"),
            x509.DNSName(u"www.mysite.com"),
            x509.DNSName(u"mysite.com"),
        ]),
        critical=False,
    ).sign(private_key, hashes.SHA256(), default_backend())

with open("certificate.csr", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))

