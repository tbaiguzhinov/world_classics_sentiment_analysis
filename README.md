# World Classics Sentiment Analysis Project

This is the home page for World Classics Sentiment Analysis project which is aimed at creating NFT using a graphical representation of positive, neutral and negative sentiment based on analysis of world classics of literature.

## Tools used

* Python and its libraries, namely: csv, Pillow, nltk (just to break down text nicely).
* Google Cloud Natural Language Processing API (NLP).

## Concept and process

The process of creating a NTF is as following:

1. Breaking down an English language version of a fiction literature work by sentences.
2. Analysis of each sentence using Google Cloud NLP. As a result we obtain a score from -1 to 1 (in realiy, -0.89(9) to 0.89(9)) and a magnitude starting from 0.
3. Based on the score, we would choose either a "positive" color for positive sentiment (I used green with RGB=0, 113, 51), a "negative" color for negative sentiment (I used red wiht RGB=148, 3, 6), or neutral (the closer the score was to 0, the higher was the alpha value, making the color transparent against a white background).

![scale](https://user-images.githubusercontent.com/49629820/156207647-92c0244d-b15d-4864-8fe6-d935581214b2.png)
5. I would get a range of pictures with a good variation of height X width and put small ellipses (pixel by pixel in size) one by one from left to right, up down.

## Example result

Here is how Tolstoy's "War and peace" looks like:

![142X170](https://user-images.githubusercontent.com/49629820/156205119-b2d701e3-868c-4dd1-994d-13febbe00876.png)

More "red" in it, right? In other words, more negative sentiment (or more war in it than peace?).

## Where to find more works?

I will be posting more works like that at opensea.io. Stay tuned!
