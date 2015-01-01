rhymer
======

Some python rhyme functions.

This is very much an early work in progress by a severley inexperienced programmer - I even hesitate to use the word *programmer*...

The current functions, rhyme and rhymes utilize the CMU Dictionary of words, phonemes and stress patterns. Rhyme simply returns a list of words that rhyme, while rhymes parses a given line and replaces each word with a random rhyme. The latter is just a proof-of-concept, really. It serves no usable purpose I can think of, except for generating nonsensical verse, and it runs pretty slow. 

Some more functions should follow, such as ones that perform simple tasks such as counting syllables and more complex ones that can determine the metre of a given line.

Since I have removed the CMU copyright info from the dictionary file the programmes call upon (cmudict_nocred.txt), here is the copyright information reproduced unedited -- the unedited file is still available in this repo:

;;; # CMUdict  --  Major Version: 0.07a [102007]
;;; 
;;; # $URL: 
;;; # $Id: cmudict.0.7a 12245 2014-02-17 18:05:41Z air $
;;; # $Rev: 12245 $  -- this is the *repository's* count; expect gaps
;;; # $Date: 2014-02-17 13:05:41 -0500 (Mon, 17 Feb 2014) $
;;; # $Author: air $
;;;
;;; #
;;; # ========================================================================
;;; # Copyright (C) 1993-2008 Carnegie Mellon University. All rights reserved.
;;; #
;;; # Redistribution and use in source and binary forms, with or without
;;; # modification, are permitted provided that the following conditions
;;; # are met:
;;; #
;;; # 1. Redistributions of source code must retain the above copyright
;;; #    notice, this list of conditions and the following disclaimer.
;;; #    The contents of this file are deemed to be source code.
;;; #
;;; # 2. Redistributions in binary form must reproduce the above copyright
;;; #    notice, this list of conditions and the following disclaimer in
;;; #    the documentation and/or other materials provided with the
;;; #    distribution.
;;; #
;;; # This work was supported in part by funding from the Defense Advanced
;;; # Research Projects Agency, the Office of Naval Research and the National
;;; # Science Foundation of the United States of America, and by member
;;; # companies of the Carnegie Mellon Sphinx Speech Consortium. We acknowledge
;;; # the contributions of many volunteers to the expansion and improvement of
;;; # this dictionary.
;;; #
;;; # THIS SOFTWARE IS PROVIDED BY CARNEGIE MELLON UNIVERSITY ``AS IS'' AND
;;; # ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
;;; # THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
;;; # PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL CARNEGIE MELLON UNIVERSITY
;;; # NOR ITS EMPLOYEES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
;;; # SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
;;; # LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
;;; # DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
;;; # THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
;;; # (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
;;; # OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
;;; #
;;; # ========================================================================



