# Auto_Summarization_Audio_NLP_GTTS

### functions:
### 1.collecting_data(data_topic, len_of_sentences=20, no_of_sentences=15):
	data_topic= Name of the topic we want the summary for.
	len_of_sentences=Number of words in one sentence.
	no_of_sentences =Total number of sentences in the summary.
It scraps data from wikipedia and then passes it for preprocessing which id done using NLTK library.The function will return a string which is the summary of the topic that was passed to the function.We can change the parameter as per our requiremnts.

### 2.text_gen(data):
It generates a text file on the same path where the code is placed. The output text file is named as "output.txt"

### 3.audio_gen(data):
It generates a mp3 voice note for the summary, it uses the gtts library for conversion.The output mp3 file is named as "result.mp3"

When we run the program, a GUI will pop-up asking for the required topic, it then feeds the topic name to the required function
