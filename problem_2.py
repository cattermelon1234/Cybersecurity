import re
import math

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

def parse_freq_text(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = construct_english_dict()
    split_text = re.split(r"\s(?=[A-Z]:\s)", msg)
    frequencies = {alphabet[i].lower(): float(item.split(": ")[1]) for i, item in enumerate(split_text)}
    return frequencies

def construct_english_dict():
    dict = {}
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        dict[letter] = 0
    return dict

def get_letter_frequencies(msg):
    freq_map = construct_english_dict()
    n = len(msg)
    for letter in msg:
        if letter in freq_map:
            freq_map[letter] += 1
    
    for key in freq_map.keys():
        freq_map[key] = freq_map[key] / n

    return freq_map

def calculate_relative_population_variance(avg_freq_map, freq_map):
    sum = 0
    for key in avg_freq_map.keys():
        sum += (freq_map[key] - avg_freq_map[key]) ** 2
    return sum / 26

def calculate_population_variance(avg, freq_map):
    sum = 0
    for key in freq_map.keys():
        sum += (freq_map[key] - avg) ** 2
    return sum / 26

def calculate_avg(dict):
    sum = 0
    for key in dict.keys():
        sum += dict[key]
    return sum / 26

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

def main():
    text = "A: 0.08167 B: 0.01492 C: 0.02782 D: 0.04253 E: 0.12702 F: 0.02228 G: 0.02015\
            H: 0.06094 I: 0.06996 J: 0.00153 K: 0.00772 L: 0.04025 M: 0.02406 N: 0.06749\
            O: 0.07507 P: 0.01929 Q: 0.00095 R: 0.05987 S: 0.06327 T: 0.09056 U: 0.02758\
            V: 0.00978 W: 0.02360 X: 0.00150 Y: 0.01974 Z: 0.00074"
    msg = "icationsservicesnowencryptcertaincommunicationsbydefaultwiththekeynece\
ssarytodecryptthecommunicationssolelyinthehandsoftheenduserthisapplies\
bothwhenthedataisinmotionoverelectronicnetworksoratrestonanelectronicd\
eviceifthecommunicationsproviderisservedwithawarrantseekingthosecommun\
icationstheprovidercannotprovidethedatabecauseithasdesignedthetechnolo\
gysuchthatitcannotbeaccessedbyanythirdpartythreatsthemoreweasasocietyr\
elyonelectronicdevicestocommunicateandstoreinformationthemorelikelyiti\
sthatinformationthatwasoncefoundinfilingcabinetslettersandphotoalbumsw\
illnowbestoredonlyinelectronicformwehaveseencaseaftercasefromhomicides\
andkidnappingstodrugtraffickingfinancialfraudandexploitationwherecriti\
calevidencecamefromsmartphonescomputersandonlinecommunicationswhenchan\
gesintechnologyhinderlawenforcementsabilitytoexerciseinvestigativetool\
sandfollowcriticalleadswemaynotbeabletoidentifyandstopterroristswhoare"
    avg_freq_map = parse_freq_text(text)
    avg = calculate_avg(avg_freq_map)
    freq_map = get_letter_frequencies(msg)
    msg_avg = calculate_avg(freq_map)
    print("Question 2A")
    population_variance = calculate_population_variance(avg, avg_freq_map)
    relative_population_variance = calculate_population_variance(msg_avg, freq_map)
    print("2a population variance: ", population_variance)
    print("Question 2B")
    print("2b relative population variance: ", relative_population_variance)
    print("QUESTION 2C")
    keys = ["yz", "xyz", "wxyz", "vwxyz", "uvwxyz"]
    for key in keys:
        encrypted = encrypt_vigenere(key, msg)
        freq_map = get_letter_frequencies(encrypted)
        encrypted_avg = calculate_avg(freq_map)
        relative_population_variance = calculate_population_variance(encrypted_avg, freq_map)
        print("key: ", key, "variance: ", relative_population_variance)
    print("QUESTION 2D")
    for key in keys:
        sum = 0
        encrypted = encrypt_vigenere(key, msg)
        ciphers = get_ciphers(len(key), encrypted)
        for cipher in ciphers:
            freq_map = get_letter_frequencies(cipher)
            encrypted_avg = calculate_avg(freq_map)
            relative_population_variance = calculate_population_variance(encrypted_avg, freq_map)
            sum += relative_population_variance
        print("key: ", key, "average variance: ", sum / len(key))
    print("QUESTION 2E")
    print(key)
    encrypted = encrypt_vigenere(key, msg)
    for x in range(2, len(key)+1):
        sum = 0
        ciphers = get_ciphers(x, encrypted)
        for cipher in ciphers:
            freq_map = get_letter_frequencies(cipher)
            encrypted_avg = calculate_avg(freq_map)
            relative_population_variance = calculate_population_variance(encrypted_avg, freq_map)
            sum += relative_population_variance
        print("length: ", x, "average variance: ", sum / x)

    print((16) * math.ceil(62 ** 8 / 1213))
if __name__ == "__main__":
    main()