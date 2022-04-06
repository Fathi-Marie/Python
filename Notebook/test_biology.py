from biology.py import *

def verif_est_base():
    assert est_base("A")
    assert not est_base("Z")
    print(ok)
verif_est_base()

def verif_est_adn():
    assert est_adn("ATGTCAAA") 
    assert not est_adn("ATBOAATG")
    print("ok")
    
verif_est_adn()

def verif_adn():
    assert arn("ATGTCAAA")== "AUGUCAAA"
    assert arn("ATGTMAAA")== "None"
    print("ok")
    
verif_adn()

def verif_arn_to_codons():
    assert arn_to_codons("CGUUAGGGG")== ["CGU","UAG","GGG"]
    assert arn_to_codons("CGUUAGGG")== ["CGU","UAG"]
    print ("OK")
verif()

