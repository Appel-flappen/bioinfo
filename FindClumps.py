from FrequentWords import FrequencyTable

def FindClumps(text, k, l, t):
    PatternList = []
    n = len(text)
    for i in range(0, n - l):
        window = text[i:i + l]
        freqMap = FrequencyTable(window, k)
        for key in freqMap.keys():
            if freqMap[key] >= t:
                PatternList.append(key)
    CleanList = list(dict.fromkeys((PatternList)))
    return CleanList

DNA = "CGGGGCCCTCTGGTATAGACCCGGCCTTGGAAGCTGTGAGCTGAACCCGTCTAAGCGCACAGTACTCTGCCCCGACCGTCGGGAGAACAGCAGCCATCACAGCTGTAAGTACGAACGGCCCCGAACCACTAGCTGAAACGTTTTTTCGGGTCCTGTATTGTATTTCAATATTACCATAATATTAATATTACCCCCTCCTAATAGTAATGGCAAATGCAACGCCAGAAGTCCTGCGCCCCGTCCGGAGATAGGTAGATGCACGGGCCTTGGGTCTGCCAACCCCACGCAAACCCCGTATATATCTGGAAGTGGGTTATCATGGGCTTCGGGCTAAACGTTCTTTGACACCGACATAGGCTGTCAGTAGCGAACATGAAACGGCGTAGTATCCATTGTAGAGGGGCTAGGGCATCCACCTCTAGAGTGGGGGTGTTTCGGCCTCGGATCAGCCGATCCCAATAAGATACTCACGTGCCGTACGACTCCACACCATGGAATTAAATGAGGGAGCCGAAGTGACGCACCCGCTGTCATGGCAGTGCGGAGACTGGTCGTGTAGTACGGCGTACGGCACGGCAGATCTGGCTTGTCCTATGGGACTGTAATCGGCCCATGTACGTTGTGAGGGATTAGTGATGTGTGGGGGGGGCTATAGGGGGGCTAGGGGCTATCTGATTCTTACGAGCACCTCGAGATCTCCGCCATTTGGTAAGCAAACGCTCCAGGCGCTGCTCCAGTGTTGCGCTGAGTAGTGTTGCGCTAAGGAGGGTTGCTCCGGCCTGGTCCAATAAGTTAACAGCGACACCAAAAAAGCCCCCTCACACTGAGCAACTACAGACGCCGGGCGGAAATACACGCCCTTTCCATCGGTCGTATCCACTAAGACCTCTTCAGGTACGGCCACACGATAATAATTGTCAAGGTCGGTCTCTGGAGTAACTTCTGGATCCCGGTCCAGCATATTGCAACCCGATGCCGGAAGCGCAAGGAGCCCACAACACGAGACACGAGAAGATGACGCATTGAGGGCATGGTATACCCGGGGGTGAGCTCCTACCATGTATCTGTTAATAGTCCTCCCTGCTAAAAAGTATACTGTGCATAATGGCCCAGGTTAAGCGCTATGTGGCTGTGGGTGAGTGTGACAACAAGATCAAGAGCACCGATCTACACTCAACAGCTGGAAGAGAAACCAATGATTCCGAGTAGGGACACTGACAACAGATGTATAAAGCGACCAACTTGAGTCTTAAAATTTGGAGCTCCCGGCCTAAGTGGGTCCGTTTCTTCTTAGAAAAAGCTGACCTGTCGAGCCTAGTCAAACGCTTGACCGCTTGACCGACCGACCCTATGACAAACGCCCGGAACCTTGGACATGCGATCAGTACGACAGTAAGTACGACAGAGTACGACTACGGGGGATGCGCAGTGAGAAGACAGAGGGACCACAGGGGAAATTTATGAACGCATACAGGCATGCCATTTGGCATGTTACTAAAAAAACAGTTAGTTAAAACAGTTGTTGAGTTAATACGATGCGTAAATACGATCTACTGGGGTGTCAGCTCCGGGGTACCATCGACCAGGTAGAATAGCCTTGCGATTGCATGCCGGTCCTATCAAAGTGTAGCAGTGGCATTCTTTTCGCCGCAAGCTTCTAGACCGAGCTCGAATATGTCGCGCTAACTGGGGAGGAGGAGTGCGGGCGGGGATATATCACCACGAAGAGTCTTTACGTCTTTACGTCTTTACGTCTTTACGTCTTTACGTCTTTACGTCTTTACGTCTTTACG"

print(*FindClumps(DNA, 8, 29, 4), sep=" ")

