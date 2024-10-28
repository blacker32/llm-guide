# RFC Standartları ve Örnekleri

RFC (Request for Comments) dokümanları, verilerin tanımlanması, biçimlendirilmesi ve iletişimi için standartları belirleyerek veri yapılarını, veri iletişim kurallarını ve protokolleri tanımlar. İşte bazı örnekleriyle birlikte en popüler veri formatları ve şemalar.

---

## 1. JSON (RFC 8259)

JSON, API’ler üzerinden veri gönderme ve alma için yaygın bir biçimdir. Örneğin, bir kullanıcının verilerini JSON formatında tutmak için:

\`\`\`json
{
  "user": {
    "id": 12345,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "address": {
      "street": "123 Main St",
      "city": "Anytown",
      "postalCode": "12345"
    }
  }
}
\`\`\`

---

## 2. XML (RFC 7303)

XML, yapılandırılmış veri taşımada kullanılır. Örneğin, bir e-ticaret sitesinde bir ürün XML ile tanımlanabilir:

\`\`\`xml
<Product>
    <ID>12345</ID>
    <Name>Wireless Mouse</Name>
    <Price>29.99</Price>
    <Description>Ergonomik tasarım, kablosuz bağlantı</Description>
    <Category>Electronics</Category>
</Product>
\`\`\`

---

## 3. MIME (RFC 2045 - 2049)

MIME, e-posta ve HTTP gibi protokollerle farklı dosya türlerini göndermek için kullanılır. Örneğin, bir HTTP isteğinde JSON içeriği gönderirken, MIME türünü belirtmek için aşağıdaki başlık kullanılır:

\`\`\`
Content-Type: application/json
\`\`\`

Bir e-posta örneği için:

\`\`\`
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 7bit

Merhaba! Bu, MIME tipi olarak düz metin bir e-posta örneğidir.
\`\`\`

---

## 4. YAML (RFC 9180)

YAML, yapılandırma dosyaları için popüler bir biçimdir. Örneğin, bir uygulama yapılandırma dosyası YAML ile tanımlanabilir:

\`\`\`yaml
database:
  host: localhost
  port: 5432
  name: example_db
  user: admin
  password: secret
\`\`\`

---

## 5. LDAP (RFC 4512 ve RFC 4519)

LDAP, kullanıcı bilgilerini saklamak için kullanılır. Örneğin, bir kullanıcıyı LDAP formatında tanımlamak:

\`\`\`
dn: cn=John Doe,ou=Users,dc=example,dc=com
objectClass: inetOrgPerson
cn: John Doe
sn: Doe
mail: johndoe@example.com
uid: johndoe
\`\`\`

---

## 6. CSV (RFC 4180)

CSV, basit tablo verileri için kullanılır. Örneğin, bir müşteri listesi CSV formatında saklanabilir:

\`\`\`csv
id,name,email
1,John Doe,johndoe@example.com
2,Jane Smith,janesmith@example.com
3,Bob Lee,boblee@example.com
\`\`\`

---

## 7. ASN.1 (RFC 5280)

ASN.1, X.509 sertifikalarında veri şemasını belirlemek için kullanılır. Örneğin, bir kimlik doğrulama sertifikasında şöyle bir yapı olabilir:

\`\`\`plaintext
Certificate  ::=  SEQUENCE  {
    tbsCertificate       TBSCertificate,
    signatureAlgorithm   AlgorithmIdentifier,
    signatureValue       BIT STRING
}
\`\`\`

---

## 8. Protobuf (Protocol Buffers)

Protobuf, Google’ın hızlı veri serileştirmesi için geliştirdiği bir sistemdir. Bir kullanıcı protokolü Protobuf ile şöyle tanımlanabilir:

\`\`\`proto
message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
\`\`\`

---

## 9. RESTful API ve HTTP Standartları (RFC 7230 - 7235)

REST API’leri genellikle JSON formatında veri döner. Örneğin, bir kullanıcının bilgilerini almak için HTTP GET isteği yapılabilir:

\`\`\`
GET /api/users/12345 HTTP/1.1
Host: api.example.com
Accept: application/json
\`\`\`

Sunucu, kullanıcının JSON verisini döndürür:

\`\`\`json
{
  "id": 12345,
  "name": "John Doe",
  "email": "johndoe@example.com"
}
\`\`\`

---

## 10. Avro (Apache Avro)

Avro, büyük veri uygulamalarında veri serileştirme için kullanılır. Bir kullanıcı kaydı için şema tanımı Avro’da şu şekilde yapılır:

\`\`\`json
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "id", "type": "int"},
    {"name": "name", "type": "string"},
    {"name": "email", "type": "string"}
  ]
}
\`\`\`

Bu Avro şeması, `User` adlı bir veri kaydını ve her alanın veri tipini tanımlar.


