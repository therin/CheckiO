# -*- coding: utf-8 -*-
'''
Oh, darn this thing.” Sofia grumbled banging her communicator device on the table.
Nikola looked up from the Hexagonal Circuit. “What’s wrong?” he walked over to where she was standing.
“The ship just sent me a message about something. I don’t really know what it was about though because this blasted thing won’t work. UGH this mega-bytes!”
“Hey, don’t overload there. Let me take a look... Sofia... You haven’t updated the encryption keys. You need to be running com-patch 7.11.89 and you’re running 5.6.13.
 Didn’t you get the emails I sent you about the updates?”
“Well... Nooooot exactly... They may have been encrypted too...”
“That’s why you keep asking to borrow my communications pad!” Interrupted Stephen.
“SIGH. Okay Sofia, I’m going to help you sort this out...”
The robots are using a very simple symmetric cipher with a special key for their correspondence with the Home Island. The text contains only lowercase letters and 
whitespaces. Each character is assigned a number which corresponds to its order in the alphabet (a whitespace is represented by 0.) The secret key is a word that has 
been translated into a sequence of numbers. That key is then applied to the block of text they wish to send.

For encryption, the value of the first letter in the block is added to the first letter in the secret key and modulo 27 (which finds the remainder of division by 27). 
This is repeated for all of the letters in the block.

For decryption, the value of the first letter in the block is reduced by number of the first letter in the secret key. If it is a negative number, add 27 to it. The 
secret key is used throughout the text blocks cyclically. After decryption, the sequence of numbers is translated into text.

For example:


Sofia does not have the current key, and has come across a new encrypted message. She still has the old encrypted and decrypted messages though, so using this 
information you must try to decrypt the new message.

Input: A list of three strings: old encrypted text, old decrypted text, new encrypted text.

Output: The string of the new decrypted text.

checkio(['lmljemxbwrhhfyd stlmhrxyvwhk',
          'this text contain the secret',
          'tsgryaaxckjqledcxhshreyuasckmysxhuwyl'
    ]) == 'and this text also contain the secret'
How it is used: Decryption software.
'''


def checkio(data):
    old_encrypted, old_decrypted, new_encrypted = data
    
    #replace this for solution
    return ''

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [
            'lmljemxbwrhhfyd stlmhrxyvwhk',
            'this text contain the secret',
            'tsgryaaxckjqledcxhshreyuasckmysxhuwyl'
        ]) == 'and this text also contain the secret', 'Secret'
    assert checkio(
        [
            'pjxxchnedonncdhhrqdgilq',
            'hello its first message',
            'pjxxchnedo jo bleyqg fsq'
        ]) == 'hello its second message', "Hello"
    assert checkio(
        [
            'dxb dxb dxb dxb',
            'bla bla bla bla',
            'tqblbefxv'
        ]) == 'real text', "Bla Bla Bla"
    assert checkio(
        [
            'dtqyefpxqtlh',
            'long message',
            'kmriy'
        ]) == 'short', "Short"
    assert checkio(
        [
            'vjwclkjfijm',
            'keyofsecret',
            'lpcmuyxhuwyd'
        ]) == 'akeyofsecret', "Almost"