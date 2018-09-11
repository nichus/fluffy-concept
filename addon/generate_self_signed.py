#!env python3

key=rsa.generate_private_key(
        public_exponent=655537,
        key_size=2048
        backend=default_backend())

# Write key here, because we'll need it later

# For self-signed subject and issuer are the same

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"splunk.mysite.com"),
    ])
cert = x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number)
            .not_valid_before(datetime.datetime.utcnow())
            .not_valid_after(
                    #10 days
                    datetime.datetime.utcnow() + datetime.timedelta(days=10)
                    )
            .add_extension(
                    x509.SubjectAlternateName([x509.DNSName(u"localhost")]),
                    critical=False,
                    )
            .sign(key, hashes.SHA256(), default_backend())

with open("certificate.pem","wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

