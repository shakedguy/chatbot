
$key = New-Object System.Security.Cryptography.RSACryptoServiceProvider(2048)
$key.ToXmlString($false) | Out-File key.pem