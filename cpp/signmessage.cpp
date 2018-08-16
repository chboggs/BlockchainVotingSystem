#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <stdio.h>
#include <string>
#include <cryptopp/rsa.h>
#include <cryptopp/osrng.h>
#include <cryptopp/base64.h>
#include <cryptopp/files.h>
#include <cryptopp/pssr.h>


std::string bytesToHex(unsigned char* data, int len) {
    std::stringstream ss;
    ss << std::hex;
    for(int i=0; i<len; ++i)
        ss << std::setw(2) << std::setfill('0') << (int)data[i];
    return ss.str();
}


std::string signMessage(const std::string& message, const std::string& privateKeyFile) {
    // Read private key
    CryptoPP::ByteQueue bytes;
    CryptoPP::FileSource file(privateKeyFile.c_str(), true);
    file.TransferTo(bytes);
    bytes.MessageEnd();
    CryptoPP::RSA::PrivateKey privateKey;
    privateKey.Load(bytes);
    // Sign message
    CryptoPP::RSASS<CryptoPP::PSS, CryptoPP::SHA1>::Signer signer(privateKey);
    size_t length = signer.MaxSignatureLength();
    CryptoPP::SecByteBlock signature(length);
    CryptoPP::AutoSeededRandomPool rng;
    length = signer.SignMessage(rng, (byte*) message.c_str(),
                                message.length(), signature);
    signature.resize(length);
    // Return a hexdump of the signature
    std::string hexDump = bytesToHex((unsigned char*)signature.data(),
                                     signature.size());
    return hexDump;
}

int main(int argc, char* argv[]) {
    std::string message(argv[1]);
    std::string privateKeyFile(argv[2]);
    std::cout << signMessage(message, privateKeyFile) << std::endl;
    return 0;
}
