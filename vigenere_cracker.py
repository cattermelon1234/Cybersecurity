
import math

def main():
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
    crack_vigenere(cipher)

def crack_vigenere(cipher):
    key = ""
    orig_cipher = cipher.lower()
    map_to_letter = construct_letter_dicts()[1]
    diff_map = parse_trigrams(cipher)
    key_lengths = find_key_length(diff_map)
    potential_keys = []

    for key_length in key_lengths:
        ciphers = get_ciphers(key_length, orig_cipher)
        for cipher in ciphers:
            letter_map = construct_freq_map(cipher)
            shift = frequency_analysis(letter_map)
            key += map_to_letter[shift]
        potential_keys.append(key)
    print(potential_keys)
    print(decrypt_vigenere(potential_keys[0], orig_cipher))
    #for key in potential_keys:
        #verify_english(decrypt_vigenere(key, orig_cipher))

def verify_english(text):
    return
def encrypt_vigenere(key, text):
    key_arr = []
    encrypted = ""
    map_to_num = construct_letter_dicts()[0]
    map_to_letter = construct_letter_dicts()[1]
    for letter in key:
        key_arr.append(map_to_num[letter])
    count = 0
    for letter in text:
        shift = key_arr[count % len(key_arr)]
        encrypted += map_to_letter[(map_to_num[letter] + shift) % 26]
        count += 1
    return encrypted

def decrypt_vigenere(key, text):
    key_arr = []
    decrypted = ""
    map_to_num = construct_letter_dicts()[0]
    map_to_letter = construct_letter_dicts()[1]
    for letter in key:
        key_arr.append(map_to_num[letter])
    count = 0
    for letter in text:
        shift = key_arr[count % len(key_arr)]
        shifted = map_to_num[letter] - shift
        if shifted < 0:
            shifted += 26
        decrypted += map_to_letter[shifted]
        count += 1
    return decrypted

def construct_letter_dicts():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    map_to_num = {}
    map_to_letter = {}
    count = 0
    for letter in alphabet:
        map_to_letter[count] = letter
        map_to_num[letter] = count
        count += 1
    return [map_to_num, map_to_letter]

def parse_trigrams(message):
    n = len(message)
    trigram_map = {}
    diff_map = {}
    for x in range(n):
        if x + 3 < n:
            if message[x:x+3] in trigram_map:
                diff_map[message[x:x+3]] = x - trigram_map[message[x:x+3]]        
            trigram_map[message[x:x+3]] = x
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
    return potential_lengths
def get_ciphers(length, message):
    ciphers = []
    for x in range(length):
        string = ""
        i = x
        while i < len(message):
            string += str(message[i])
            i += length
        ciphers.append(string)
    return ciphers
def euclidean_distance(map_a, map_b):
    sum = 0
    for key in map_a.keys():
        sum += (map_a[key] - map_b[key]) ** 2
    return math.sqrt(sum)

def frequency_analysis(msg_freq):
    english_freq_map = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 
        'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06996, 'j': 0.00153, 
        'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 
        'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 
        'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 
        'z': 0.00074
    }
    map_to_num = construct_letter_dicts()[0]
    map_to_letter = construct_letter_dicts()[1]
    min = 100
    shift = 0
    for x in range(26):
        new_map = {}
        for key in msg_freq.keys():
            new_map[map_to_letter[(map_to_num[key] - x) % 26]] = msg_freq[key]
        dist = euclidean_distance(new_map, english_freq_map)
        if dist < min:
            min = dist
            shift = x
    return shift
    
def construct_freq_map(message):
    letter_map = {}
    for letter in message:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1
    return letter_map
    
if __name__ == "__main__":
    main()