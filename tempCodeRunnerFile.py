
def main():
    """
    arr = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in arr:
        for b in range(26):
            print(decrypt_affine_cipher(a, b, "xjefquvfszpvilz"))
    """
    cipher = "NLLPRAOZLSETDRVUTPKMPEDEVKNZKOEVKTZZUDYRGPZUFETTLJFBYZIYGVLMZINRSARJENFUOQOCCVHLMZYLDLRMIASRZBIIOXVHSIIOYUYAXKPZNLRMZSEIHDIJEQZJIXGNOZASJOSNRSDILINZAAVKAEEPGLZMLILPVUPZIAISTSYFDIRZHPUHYWUFEYLFVKEXRYKIZWSVUOYXCZLUTVEWLJHTSVIYUBSXXILCWOAKREYLRICADRJCSANERIIPOTJKVTLKSEFJKLULOVYTLKCL\
IUEKOEDKOEQKLWFUSXNEXVUTLGTMLPLXZHTJNRIGTTEKUWZRTRSEQVICVTAHKSFILOJOTM\
VJAYYETKDAWZHPZYMSTEJRASXGKPKVDEEMLEHGISEYKOAWTODKHKIONEYLCSSPLEFAPRTZ\
XLTLKREYLSISEYJPTXONRLWHIXEAFPNXONRKVTIRDLITARGGPDLNXUWYCLSWZHLEWEVIEY\
KVFXNENFTPETYLEKWLKRPUVEWSRNIVMAKLWGBTLOSXZSLMUNOFSLEXSLCHRCTOEZUTIRDL\
IZTSIKSVVWRYLPJZTLGNAVYCITTJFBOATTSVJOQVAYPAHEZSCZNHXEOFKOEWZONBOOPJEC\
RUDCUULILAPRBPZUGVUYLCSYWIRPNLDSBECSFTLKSPKOEWKBFILAYIRLKZWMZHEYLIVYTP\
RRLYTCSVZTLKICYBNXONRRUDJOSSZUGXXIAJAHIORNFYPSXAEVQEXYAYUNOPJEYGHREIHF\
KLSXNIDZZARUUEIHGIEOFILOYZOQCPNIMEVBVTIRDLIWATKRXIJRSSWPCSTIRDLIWATKRS\
RZDMLFPILNXBINVWRIYIOVUTWKANYLAVTIYXVVIXTSFBSETDOFSLEXSLPLAVTOHZOAZKSA\
VUTXNEWRZTXCOXFUTLYAYRSYDONRNOAXGLWKOEWKGFPZDSGNOZZTMRLNRUTJOGFILIXUUE\
FUEXNIYXPDSQNZNPSXNAEFBRTGPPIJOQVAYPSOWZMTCSISTDZCSAVYLLJAYIGRLEKIPRBP\
KAHEZHLCMOJZHLKDAWYPPEAIRGLWKOETGPPIDOVQGZZUGFGCVRUDJUREYIEXCEPEHLPZHP\
JLVMIEAILSMJEYKZGIQKZKOERKWWRDOJKVZCBTMUNTEJOVVOCRAEESECZJAWKEXJAOFKSF\
ICIZGLZWAHIANQZATIYTHVSLMTMJSVOOEOFVPTLKROFPTVOGSKVRCUURVAEPOMTEHTIJIY"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    map_to_num = {}
    map_to_letter = {}
    count = 0
    for letter in alphabet:
        map_to_letter[count] = letter
        map_to_num[letter] = count
        count += 1
    diff_map = parse_trigrams(cipher)
    find_key_length(diff_map)
    ciphers = get_ciphers(7, cipher)
    for cipher in ciphers:
        letter_map = get_common_letters(cipher)
        print(letter_map)

#rhpegal
#rhaegal
def encrypt_affine_cipher(a, b, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    map_to_num = {}
    map_to_letter = {}
    count = 0
    for letter in alphabet:
        map_to_letter[count] = letter
        map_to_num[letter] = count
        count += 1
    
    message_arr = [map_to_num[l] for l in message]
    encrypted = ""
    for num in message_arr:
        encrypted += map_to_letter[(num * a + b) % 26]
    return encrypted

def decrypt_affine_cipher(a, b, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    map_to_num = {}
    map_to_letter = {}
    count = 0
    a_inverse = pow(a, -1, 26)
    for letter in alphabet:
        map_to_letter[count] = letter
        map_to_num[letter] = count
        count += 1
    message_arr = [map_to_num[l] for l in message]
    decrypted = ""
    for num in message_arr:
        decrypted += map_to_letter[((num - b) * a_inverse) % 26]
    return decrypted
def parse_trigrams(message):
    n = len(message)
    trigram_map = {}
    diff_map = {}
    for x in range(n):
        if x + 3 < n:
            if message[x:x+3] in trigram_map:
                diff_map[message[x:x+3]] = x - trigram_map[message[x:x+3]]        
            trigram_map[message[x:x+3]] = x
    for key in diff_map.keys():
        print("trigram: ", key, " diff: ", diff_map[key])
    return diff_map
def find_key_length(diff_map):
    num = 0
    total = 0
    potential_lengths = []
    for x in range(2, 25):
        for key in diff_map.keys():
            total += 1
            if diff_map[key] % x == 0:
                num += 1
        if (num / total > 0.5):
            potential_lengths.append(x)
        num = 0
        total = 0
    print(potential_lengths)
def get_ciphers(length, message):
    ciphers = []
    for x in range(length):
        string = ""
        i = x
        while i < len(message):
            string += str(message[i])
            i += length
        ciphers.append(string)
        print(string)
    return ciphers
def frequency_analysis(msg_freq):
    english_freq_map = {
        'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 
        'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06996, 'J': 0.00153, 
        'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 
        'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 
        'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 
        'Z': 0.00074
    }
    
def get_common_letters(message):
    letter_map = {}
    for letter in message:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1
    return letter_map
    
if __name__ == "__main__":
    main()