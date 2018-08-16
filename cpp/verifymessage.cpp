#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <cryptopp/rsa.h>
#include <cryptopp/osrng.h>
#include <cryptopp/base64.h>
#include <cryptopp/files.h>
#include <cryptopp/pssr.h>


std::vector<char> hexToBytes(const std::string& hex) {
    std::vector<char> bytes;
    for (unsigned int i = 0; i < hex.length(); i += 2) {
        std::string byteString = hex.substr(i, 2);
        char byte = (char) strtol(byteString.c_str(), NULL, 16);
        bytes.push_back(byte);
    }
    return bytes;
}

bool verifyMessage(const std::string& message, const std::string& signature,
                   const std::string& publicKeyFile) {
    //Read public key
	CryptoPP::ByteQueue bytes;
	CryptoPP::FileSource file(publicKeyFile.c_str(), true);
	file.TransferTo(bytes);
	bytes.MessageEnd();
	CryptoPP::RSA::PublicKey publicKey;
	publicKey.Load(bytes);
    // Verifiy
    std::vector<char> sigBytes = hexToBytes(signature);
    CryptoPP::SecByteBlock sigBlock((byte*)&sigBytes[0], sigBytes.size());
    CryptoPP::RSASS< CryptoPP::PSS,  CryptoPP::SHA1>::Verifier verifier(publicKey);
    bool result = verifier.VerifyMessage((byte*)message.c_str(),
        message.length(), sigBlock, sigBlock.size());
    return result;
}


int main(int argc, char* argv[]) {
    std::string message(argv[1]);
    std::string signature(argv[2]);
    std::string publicKeyFile(argv[3]);
    std::cout << verifyMessage(message, signature, publicKeyFile) << std::endl;
    return 0;
}
