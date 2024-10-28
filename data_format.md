Data URI Scheme dışında, verileri metin formatına dönüştürmek ve taşımak için çeşitli standart genel şemalar mevcuttur. Bu şemalar, farklı türdeki verileri (metin, resim, video, ses) güvenli ve etkili bir şekilde aktarmak için tasarlanmıştır. İşte bazı önemli alternatif şemalar:

### 1. **Base64**
- **Açıklama:** Binary veriyi ASCII metin formatına dönüştürür. 3 baytı 4 karaktere dönüştürür.
- **Örnek:**
  ```python
  data = "data:audio/mpeg;base64,AAAAIGZ0eXBtcDQyAAAAAG1wNDJpc29tYXZj..."
  ```

### 2. **Base32**
- **Açıklama:** Base64'e göre daha az karakter seti kullanır (32 karakter yerine 64 karakter). Daha okunabilir ve hata toleransı yüksek.
- **Örnek:**
  ```python
  import base64
  data = "data:audio/mpeg;base32," + base64.b32encode(b'example data').decode()
  ```

### 3. **Base85 (Ascii85)**
- **Açıklama:** Base64'e göre daha verimli bir kodlama yöntemidir. 4 baytı 5 karaktere dönüştürür.
- **Örnek:**
  ```python
  import base64
  data = "data:audio/mpeg;base85," + base64.a85encode(b'example data').decode()
  ```

### 4. **Hex (Hexadecimal)**
- **Açıklama:** Her bayt, iki onaltılık (hexadecimal) karaktere dönüştürülür. Daha basit ve hata toleransı yüksek.
- **Örnek:**
  ```python
  data = "data:audio/mpeg;hex," + b'example data'.hex()
  ```

### 5. **URL Encoding (Percent Encoding)**
- **Açıklama:** URL'lerde kullanılmak üzere özel karakterleri `%` işareti ve onaltılık değerlerle temsil eder. ASCII karakter setini kullanır.
- **Örnek:**
  ```python
  from urllib.parse import quote
  data = "data:audio/mpeg;url," + quote(b'example data')
  ```

### 6. **MIME (Multipurpose Internet Mail Extensions)**
- **Açıklama:** E-posta ve HTTP gibi protokollerde farklı türdeki verileri taşımak için kullanılır. MIME türleri, verinin türünü belirtir (örneğin, `image/png`, `video/mp4`).
- **Örnek:**
  ```python
  data = "Content-Type: audio/mpeg\n\n" + b'example data'
  ```

### 7. **JSON (JavaScript Object Notation)**
- **Açıklama:** Verileri metin formatında taşımak için kullanılan hafif bir veri formatıdır. JSON, JavaScript nesnelerini temsil etmek için tasarlanmıştır, ancak birçok programlama dilinde desteklenir.
- **Örnek:**
  ```python
  import json
  data = json.dumps({"type": "audio/mpeg", "data": "example data"})
  ```

### 8. **XML (eXtensible Markup Language)**
- **Açıklama:** Verileri yapısallaştırmak ve taşımak için kullanılan metin tabanlı bir dil. XML, verileri etiketler kullanarak yapısallaştırır.
- **Örnek:**
  ```python
  data = "<audio type='mpeg'>example data</audio>"
  ```

### 9. **YAML (YAML Ain't Markup Language)**
- **Açıklama:** Verileri metin formatında taşımak için kullanılan hafif bir veri formatıdır. YAML, insanlar tarafından okunabilir ve yazılabilir olacak şekilde tasarlanmıştır.
- **Örnek:**
  ```python
  data = "type: audio/mpeg\ndata: example data"
  ```

### 10. **Protocol Buffers (protobuf)**
- **Açıklama:** Google tarafından geliştirilmiş, verileri serileştirmek ve taşımak için kullanılan bir dil ve platform bağımsız mekanizmadır. Protobuf, verimli ve hızlı veri serileştirme sağlar.
- **Örnek:**
  ```python
  from google.protobuf import json_format
  from my_protobuf_file_pb2 import AudioMessage

  message = AudioMessage(type='mpeg', data=b'example data')
  data = message.SerializeToString()
  ```

### 11. **MessagePack**
- **Açıklama:** JSON'a benzer, ancak daha verimli bir veri serileştirme formatıdır. MessagePack, küçük ve hızlı veri serileştirme sağlar.
- **Örnek:**
  ```python
  import msgpack
  data = msgpack.packb({"type": "audio/mpeg", "data": b'example data'})
  ```

### 12. **CBOR (Concise Binary Object Representation)**
- **Açıklama:** JSON'a benzer, ancak daha verimli bir ikili veri serileştirme formatıdır. CBOR, küçük ve hızlı veri serileştirme sağlar.
- **Örnek:**
  ```python
  import cbor2
  data = cbor2.dumps({"type": "audio/mpeg", "data": b'example data'})
  ```

### 13. **BSON (Binary JSON)**
- **Açıklama:** JSON'a benzer, ancak ikili formatta bir veri serileştirme formatıdır. BSON, MongoDB gibi NoSQL veritabanları tarafından kullanılır.
- **Örnek:**
  ```python
  import bson
  data = bson.dumps({"type": "audio/mpeg", "data": b'example data'})
  ```

### 14. **Avro**
- **Açıklama:** Apache Avro, verileri serileştirmek ve taşımak için kullanılan bir veri serileştirme sistemidir. Avro, şemaları kullanarak verileri yapısallaştırır ve verimli serileştirme sağlar.
- **Örnek:**
  ```python
  from avro.datafile import DataFileWriter
  from avro.io import DatumWriter
  from avro.schema import parse

  schema = parse('{"type": "record", "name": "AudioMessage", "fields": [{"name": "type", "type": "string"}, {"name": "data", "type": "bytes"}]}')
  with DataFileWriter(open("audio_message.avro", "wb"), DatumWriter(), schema) as writer:
      writer.append({"type": "audio/mpeg", "data": b'example data'})
  ```

### 15. **Thrift**
- **Açıklama:** Apache Thrift, verileri serileştirmek ve taşımak için kullanılan bir veri serileştirme sistemidir. Thrift, farklı diller ve platformlar arasında veri aktarımı için kullanılır.
- **Örnek:**
  ```python
  from thrift.protocol import TBinaryProtocol
  from thrift.transport import TTransport
  from my_thrift_file import AudioMessage

  message = AudioMessage(type='mpeg', data=b'example data')
  transport = TTransport.TMemoryBuffer()
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  message.write(protocol)
  data = transport.getvalue()
  ```

### Sonuç
