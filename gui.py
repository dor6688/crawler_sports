import os
import time
from tkinter import *
import tkinter
import tkinter.messagebox
from tkinter import filedialog
import queue
import shutil
from tkinter.filedialog import askopenfilename


def __init__(root):
    topFrame = Frame(root)
    window_width = 300
    window_height = 370
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.title("crawler_sport")
    root.geometry("300x370+{}+{}".format(position_right, position_down))
    root.resizable(0, 0)
    text_subject = Label(root, text="Subject:")
    subject = Entry(root)
    button1 = Button(text="Browse...", fg='black', command=lambda: sport_five())
    button2 = Button(text="Browse...", fg='black', command=lambda: sport_one())
    button3 = Button(text="Browse...", fg='black', command=lambda: one_sport())
    text_subject.grid(row=0)
    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)

    # text_Queries_Path = Label(root, text="Queries Path:")
    # text_Query = Label(root, text="Query:")
    # entry_Queries_Path = Entry(root)
    # entry_Query = Entry(root)
    # queryButton = Button(text="Browse...", fg='black', command=lambda: browse_queries_folder())
    # runButton = Button(text="Run", fg='black', command=lambda: start_search())
    # text_Queries_Path.grid(row=5)
    # text_Query.grid(row=6)
    # entry_Queries_Path.grid(row=5, column=1)
    # entry_Query.grid(row=6, column=1)
    # runButton.grid(row=7, column=1)
    # queryButton.grid(row=5, column=2)
    # entry_Semantic_Bool = tkinter.IntVar()
    # semanticLabel = Checkbutton(root, text="Semantic", variable=entry_Semantic_Bool)
    # semanticLabel.grid(row=7, column=0)
    # cityButton = Button(text="Cities Filter", fg='black', command=lambda: city_filter())
    # cityButton.grid(row=4, column=1)
    #
    # language = Label(root, text="Language:")
    # language.grid(row=8, column=0)
    # language_list = Listbox(root, width=20, height=5)
    # language_list.grid(row=8, column=1)
    # reset_button = Button(text="Reset", fg='black', command=lambda: reset())
    # reset_button.grid(row=9, column=1)
    # dictionary_button = Button(text="Show Dictionary", fg='black', command=lambda: show_dictionary())
    # dictionary_button.grid(row=10, column=1)
    # load_dictionary_button = Button(text="Load Dictionary", fg='black',
    #                                 command=lambda: load_dictionary())
    # load_dictionary_button.grid(row=11, column=1)
    # text_status_label = Label(root, text="Status: ")
    # status_text_string = StringVar()
    # text_status = Label(root, textvariable=status_text_string, fg="blue")
    # status_text_string.set("Ready to start")
    # text_status_label.grid(row=12, column=0)
    # text_status.grid(row=12, column=1)
    #
    # city_into_query = ""


def sport_five():
    print("Sport5")


def sport_one():
    print("Sport1")


def one_sport():
    print("One")

#
# # need to add the paths and the errors
# def start_work(self):
#     global main_dictionary
#     global number_of_docs
#     global total_length_of_docs
#     global avgdl
#     main_dictionary = {}
#     number_of_docs = 0
#     total_length_of_docs = 0
#     avgdl = 0
#     if self.subject.get() == '' or self.entry_Save_Path.get() == '':
#         tkinter.messagebox.showerror("Error", "Please fill in Resources Path and Save Path")
#         # self.subject = ''
#         # self.entry_Save_Path = ''
#
#     else:
#         self.status_text_string.set("Loading, please wait...")
#         self.text_status.config(fg="Red")
#
#         start = time.time()
#
#         # # print("work on it")
#         # if self.entry_Stemming_Bool.get() == 1:
#         #     print("with stemmer")
#         # else:
#         #     print("without stemmer")
#
#         root_folder_path = g.subject.get()
#         stop_words_path = root_folder_path + '/stop_words.txt'
#         save_path = g.entry_Save_Path.get()
#
#         # lock = multiprocessing.Lock()
#
#         # processes = []
#
#         stemming_bool = self.entry_Stemming_Bool.get()
#         read_file = ReadFile(root_folder_path)
#         number_of_threads = len(read_file.file_names_split)
#         read_file.read_city_language(save_path)
#
#         self.language_list.delete(0, END)
#         for language in sorted(read_file.language_dictionary):
#             self.language_list.insert(END, language)
#
#         # for city in sorted(read_file.cities):
#         #     self.list_cities.add(city)
#
#         main_index.set_stemming_bool(stemming_bool)
#
#         for city in read_file.cities:
#             cities_posting[city] = {}
#
#         # ------ Parsing Without Threads ------
#
#         for iteration_index in range(number_of_threads):
#             (docs_texts, docs_properties) = read_file.read()
#             parser = Parse(iteration_index, stop_words_path, stemming_bool, read_file.cities)
#             parser.parse(docs_texts, docs_properties)
#             # print('Done Parse %d' % iteration_index)
#
#         # ------ Parsing With Threads ------
#
#         # for thread_index in range(number_of_threads):
#         #     process = Process(target=concurrent_parsing, args=[read_file, stop_words_path, thread_index])
#         #     process.start()
#         #     processes.append(process)
#         #
#         # # Finish threads
#         # for process in processes:
#         #     process.join()
#
#         # ------ Indexing Without Threads ------
#
#         # print('Start Updating Cities Posting')
#
#         cp = open((self.entry_Save_Path.get() + '/cities_posting.txt'), 'w')
#         for key in sorted(cities_posting.keys()):
#             cp.write(key + str(cities_posting[key]).replace(' ', '') + '\n')
#
#         # print('Done Updating Cities Posting')
#
#         ending = ''
#         if stemming_bool:
#             ending = '_with_stemming'
#
#         avgdl = float(total_length_of_docs) / number_of_docs
#
#         # print('Start Indexing')
#
#         indexer_index = 0
#         q = queue.Queue()
#
#         for i in range(number_of_threads):
#             q.put(('parser_%d_terms' % i) + ending + '.txt')
#
#         # print('Start Merging')
#
#         final_merged_file_path = ''
#
#         while q.qsize() > 1:
#             q.put(main_index.merge_two_posting_files(q.get(), q.get(), indexer_index))
#             indexer_index += 1
#
#         # print('Done Merging')
#
#         if indexer_index == 0:
#             final_merged_file_path = ('parser_0_terms%s.txt' % ending)
#         else:
#             final_merged_file_path = (('merge%d' % (indexer_index - 1)) + ending + '.txt')
#
#         main_index.build_index_dictionary(save_path, final_merged_file_path)
#
#         if os.path.exists(save_path + '/posting%s.txt' % ending):
#             os.remove(save_path + '/posting%s.txt' % ending)
#         os.rename(final_merged_file_path, 'posting%s.txt' % ending)
#         shutil.move('posting%s.txt' % ending, save_path)
#
#         # os.rename(save_path + '/' + final_merged_file_path, save_path + '/posting%s.txt' % ending)
#         # shutil.move(final_merged_file_path, root_folder_path)
#         # shutil.move(root_folder_path + '/' + final_merged_file_path, save_path)
#
#         docs_file_name = ('parser_docs' + ending + '.txt')
#         docs_file = open(docs_file_name, "ab")
#         # for doc in sorted(docs_dictionary.keys(), key=str.lower):
#         for doc in docs_dictionary.keys():
#             str_max_tf = str(docs_dictionary[doc]['max_tf'])
#             str_max_term = str(docs_dictionary[doc]['max_term'])
#             str_num_of_terms = str(docs_dictionary[doc]['num_of_terms'])
#             str_doc_length = str(docs_dictionary[doc]['doc_length'])
#             str_doc_entities = str(docs_dictionary[doc]['entities'])
#             docs_file.write("<" + doc + "~" + str_max_tf + "~" + str_max_term + '~'
#                             + str_num_of_terms + "~" + docs_dictionary[doc]['doc_city'] + "~"
#                             + str_doc_length + "~" + str_doc_entities.replace(' ', '') + ">\n")
#         docs_file.write("@@@")
#         docs_file.close()
#
#         if os.path.exists(save_path + '/parser_docs%s.txt' % ending):
#             os.remove(save_path + '/parser_docs%s.txt' % ending)
#         shutil.move('parser_docs%s.txt' % ending, save_path)
#
#         # if os.path.exists(save_path + '/posting%s.txt' % ending):
#         #     os.remove(save_path + '/posting%s.txt' % ending)
#
#         erase_index = 0
#
#         while os.path.exists('parser_%d_terms.txt' % erase_index):
#             os.remove('parser_%d_terms.txt' % erase_index)
#             erase_index += 1
#         erase_index = 0
#         while os.path.exists('parser_%d_terms_with_stemming.txt' % erase_index):
#             os.remove('parser_%d_terms_with_stemming.txt' % erase_index)
#             erase_index += 1
#         erase_index = 0
#         while os.path.exists('merge%d.txt' % erase_index):
#             os.remove('merge%d.txt' % erase_index)
#             erase_index += 1
#         erase_index = 0
#         while os.path.exists('merge%d_with_stemming.txt' % erase_index):
#             os.remove('merge%d_with_stemming.txt' % erase_index)
#             erase_index += 1
#
#         while not q.empty():
#             q.get()
#
#         # print('Done Indexing')
#
#         finish = time.time()
#
#         self.status_text_string.set("Done!")
#         self.text_status.config(fg="Green")
#
#         finish_window = Toplevel(root)
#         window_width = 250
#         window_height = 100
#         position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
#         position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
#         finish_window.geometry("250x100+{}+{}".format(position_right, position_down))
#         num_of_docs_label = Label(finish_window, text="Number of indexed documents: %d" % number_of_docs)
#         num_of_terms_label = Label(finish_window,
#                                    text="Number of unique terms: %d" % (len(main_dictionary.keys())))
#         total_runtime = float("{0:.2f}".format(finish-start))
#         runtime_label = Label(finish_window, text=("Total Runtime (seconds): %s" % total_runtime))
#         num_of_docs_label.grid(row=0, column=1)
#         num_of_terms_label.grid(row=1, column=1)
#         runtime_label.grid(row=2, column=1)
#
#
# def start_search(self):
#     global docs_dictionary
#     if self.entry_Queries_Path.get() == '' and self.entry_Query.get() == '' and self.city_into_query == '':
#         tkinter.messagebox.showerror("Error", "Please fill Query or Queries Path")
#     elif len(docs_dictionary.keys()) == 0:
#         tkinter.messagebox.showerror("Error", "Please load dictionaries")
#     elif self.subject.get() == '':
#         tkinter.messagebox.showerror("Error", "Please fill resources path so we can get the stop words")
#     else:
#         search_results_window = Toplevel(root)
#         # save_queries_results_window = Toplevel(root)
#         window_width = 250
#         window_height = 500
#         position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
#         position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
#         search_results_window.geometry("250x500+{}+{}".format(position_right, position_down))
#         # save_queries_results_window.geometry("150x250+{}+{}".format(position_right, position_down))
#         ranker = 0
#
#         # init the stemming and the stop words path
#         stop_words_path = self.subject.get() + '/stop_words.txt'
#         stemming_bool = self.entry_Stemming_Bool.get()
#         semantic_bool = self.entry_Semantic_Bool.get()
#
#         # one query from the entry query
#         if self.entry_Query.get() != '' or (self.city_into_query != '' and self.entry_Query.get() == ''):
#             self.number_of_individual_queries += 1
#             q = str(self.entry_Query.get()) + " " + str(self.city_into_query)
#             query_after_parsing = []
#             query_tokens = []
#             # //////////////////////////////////////////
#             # check if we need to fill the entries again
#             # //////////////////////////////////////////
#
#             parser = Parse(0, stop_words_path, stemming_bool, "")
#             query_tokens = parser.get_tokens(q)
#             query_after_parsing = parser.parse_document("only_one_query", query_tokens)
#             new_query_after_parsing = " ".join(query_after_parsing)
#             searcher = Searcher(new_query_after_parsing, self.entry_Semantic_Bool.get())
#             searcher.docs_containing_current_terms.clear()
#             searcher.find_docs_containing_current_terms()
#             ranker = Ranker(searcher.docs_containing_current_terms, searcher.query_terms)
#             ranker.rank()
#
#             frame1 = Frame(search_results_window)
#             frame1.pack()
#
#             results_save_button = Button(frame1, text="Save Results",
#                                          command=lambda: self.save_query_results
#                                          (": %d" % self.number_of_individual_queries,
#                                           ranker.ranked_docs))
#             results_save_button.pack(side="top")
#
#             frame2 = Frame(search_results_window)
#             frame2.pack()
#
#             vsb = Scrollbar(search_results_window, orient="vertical")
#             text = Text(search_results_window, width=40, height=20, yscrollcommand=vsb.set)
#             vsb.config(command=text.yview)
#             vsb.pack(side="right", fill="y")
#             text.pack(side="left", fill="both", expand=True)
#
#             i = 1
#             for doc_tuple in ranker.ranked_docs:
#                 doc_index = Label(search_results_window, text="%d." % i)
#                 i += 1
#                 doc_name = doc_tuple[0]
#                 doc_button = Button(search_results_window, text=doc_name,
#                                     command=lambda doc_name=doc_name: self.doc_entities(doc_name))
#                 text.window_create("end", window=doc_index)
#                 text.window_create("end", window=doc_button)
#                 text.insert("end", "\n")
#
#             # if len(ranker.relevant_docs.keys()) > 0:
#             #     i = 0
#             #     minimum_score = 0.5
#             #     current_score = ranker.ranked_docs[i][1]
#             #     while current_score > minimum_score and i < 50:
#             #         doc_index = Label(search_results_window, text="%d." % (i + 1))
#             #         doc_name = ranker.ranked_docs[i][0]
#             #         doc_button = Button(search_results_window, text=doc_name,
#             #                             command=lambda doc_name=doc_name: self.doc_entities(doc_name))
#             #         text.window_create("end", window=doc_index)
#             #         text.window_create("end", window=doc_button)
#             #         text.insert("end", "\n")
#             #         i += 1
#             #         current_score = ranker.ranked_docs[i][1]
#
#             # rank_range = min(50, len(ranker.docs_ranks)) + 1
#             # for i in range(1, rank_range):
#             #     doc_index = Label(search_results_window, text="%d." % i)
#             #     doc_name = ranker.docs_ranks[i - 1][0]
#             #     doc_button = Button(search_results_window, text=doc_name,
#             #                         command=lambda doc_name=doc_name: self.doc_entities(doc_name))
#             #     text.window_create("end", window=doc_index)
#             #     text.window_create("end", window=doc_button)
#             #     text.insert("end", "\n")
#
#         # many queries from queries doc
#         else:
#             queries_results_after_all = {}
#             queries = self.get_queries_from_doc()
#             for query_number in queries:
#                 q = queries[query_number]['query_text']
#                 parser = Parse(0, stop_words_path, stemming_bool, "")
#                 query_tokens = parser.get_tokens(q)
#                 query_doc_name = "query " + query_number
#                 query_after_parsing = parser.parse_document(query_doc_name, query_tokens)
#                 new_query_after_parsing = " ".join(query_after_parsing)
#                 searcher = Searcher(new_query_after_parsing, self.entry_Semantic_Bool.get())
#                 searcher.docs_containing_current_terms.clear()
#                 searcher.find_docs_containing_current_terms()
#                 ranker = Ranker(searcher.docs_containing_current_terms, searcher.query_terms)
#                 ranker.rank()
#                 queries_results_after_all[query_number] = []
#                 for doc in ranker.ranked_docs:
#                     queries_results_after_all[query_number].append(doc[0])
#
#             frame1 = Frame(search_results_window)
#             frame1.pack()
#             queries_alert = Label(frame1, text="Boogle has finished searching!")
#             queries_alert.pack(side="top")
#             queries_alert = Label(frame1, text="Please save the results:")
#             queries_alert.pack(side="top")
#             queries_results_save_button = Button(frame1, text="Save Results",
#                                          command=lambda queries_results_after_all=queries_results_after_all:
#                                          self.save_queries_results(queries_results_after_all))
#             queries_results_save_button.pack(side="top")
#             # if len(ranker.relevant_docs.keys()) > 0:
#             #     i = 0
#             #     minimum_score = 0.5
#             #     current_score = ranker.ranked_docs[i][1]
#             #     while current_score > minimum_score and i < 50:
#             #         doc_index = Label(search_results_window, text="%d." % (i + 1))
#             #         doc_name = ranker.ranked_docs[i][0]
#             #         doc_button = Button(search_results_window, text=doc_name,
#             #                             command=lambda doc_name=doc_name: self.doc_entities(doc_name))
#             #         text.window_create("end", window=doc_index)
#             #         text.window_create("end", window=doc_button)
#             #         text.insert("end", "\n")
#             #         i += 1
#             #         current_score = ranker.ranked_docs[i][1]
#
#             # rank_range = min(50, len(ranker.docs_ranks)) + 1
#             # for i in range(1, rank_range):
#             #     doc_index = Label(search_results_window, text="%d." % i)
#             #     doc_name = ranker.docs_ranks[i - 1][0]
#             #     doc_button = Button(search_results_window, text=doc_name,
#             #                         command=lambda doc_name=doc_name: self.doc_entities(doc_name))
#             #     text.window_create("end", window=doc_index)
#             #     text.window_create("end", window=doc_button)
#             #     text.insert("end", "\n")
#
#
# def browse_save_file(self):
#     if len(self.entry_Save_Path.get()) > 0:
#         self.entry_Save_Path.delete(0, len(root.file_save_name))
#     # print("choose a folder")
#     root.file_save_name = filedialog.askdirectory()
#     self.entry_Save_Path.insert(0, root.file_save_name)
#     # print(root.file_save_name)
#
#
# def browse_folder(self):
#     if len(self.subject.get()) > 0:
#         self.subject.delete(0, len(root.folder_name))
#     # print("choose a folder")
#     root.folder_name = filedialog.askdirectory()
#     self.subject.insert(0, root.folder_name)
#     # print(root.folder_name)
#
#
# def browse_queries_folder(self):
#     if len(self.entry_Queries_Path.get()) > 0:
#         self.entry_Queries_Path.delete(0, len(root.queries_folder_name))
#     # print("choose a folder")
#     root.queries_folder_name = askopenfilename()
#     self.entry_Queries_Path.insert(0, root.queries_folder_name)
#     # print(root.queries_folder_name)
#
#
# def reset(self):
#     global main_dictionary
#     #     need to delete thus label from the label
#     if self.entry_Save_Path.get() == '':
#         tkinter.messagebox.showerror("Error", "Please fill in a Save Path")
#     else:
#         if self.subject is not None:
#             self.subject.delete(0, END)
#         if self.entry_Save_Path is not None:
#             self.entry_Save_Path.delete(0, END)
#         self.language_list.delete(0, END)
#         main_dictionary = {}
#
#         if os.path.exists(root.file_save_name + '/posting.txt'):
#             os.remove(root.file_save_name + '/posting.txt')
#         if os.path.exists(root.file_save_name + '/posting_with_stemming.txt'):
#             os.remove(root.file_save_name + '/posting_with_stemming.txt')
#         if os.path.exists(root.file_save_name + '/index.txt'):
#             os.remove(root.file_save_name + '/index.txt')
#         if os.path.exists(root.file_save_name + '/index_with_stemming.txt'):
#             os.remove(root.file_save_name + '/index_with_stemming.txt')
#         if os.path.exists(root.file_save_name + '/cities_index.txt'):
#             os.remove(root.file_save_name + '/cities_index.txt')
#         if os.path.exists(root.file_save_name + '/cities_posting.txt'):
#             os.remove(root.file_save_name + '/cities_posting.txt')
#         # print("restarting")
#
#
# @staticmethod
# def show_dictionary():
#     # print("Show Dictionary")
#     global main_dictionary
#     if len(main_dictionary.keys()) == 0:
#         tkinter.messagebox.showerror("Error", "There is no dictionary loaded")
#     else:
#         window = Toplevel(root)
#         window_width = 300
#         window_height = 275
#         position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
#         position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
#         window.geometry("300x275+{}+{}".format(position_right, position_down))
#         index_list = Listbox(window, width=window.winfo_width(), height=window.winfo_height())
#         index_list.delete(0, END)
#         index_list.pack(side="left", fill="both", expand=1)
#         scrollbar = Scrollbar(window, orient="vertical")
#         scrollbar.config(command=index_list.yview)
#         scrollbar.pack(side="right", fill="y")
#         index_list.config(yscrollcommand=scrollbar.set)
#         # index_lines = open(self.entry_Save_Path.get() + ('/index%s.txt' % ending), 'r').readlines()
#         index_list.insert(END, "Term     ->     TF")
#         for key in sorted(main_dictionary.keys(), key=str.lower):
#             index_list.insert(END, key + '     ->     ' + main_dictionary[key]['tf'])
#
#
# def load_dictionary(self):
#     # print("Load Dictionary")
#     global main_dictionary
#     global docs_dictionary
#     global avgdl
#     ending = ''
#     if self.entry_Stemming_Bool.get():
#         ending = '_with_stemming'
#     if not os.path.exists(self.entry_Save_Path.get() + ('/index%s.txt' % ending)):
#         tkinter.messagebox.showerror("Error", "There is no dictionary in the specified Save Path")
#     elif not os.path.exists(self.entry_Save_Path.get() + '/parser_docs.txt'):
#         tkinter.messagebox.showerror("Error", "There is no documents dictionary in the specified Save Path")
#     elif not os.path.exists(self.entry_Save_Path.get() + '/languages.txt'):
#         tkinter.messagebox.showerror("Error", "There is no languages dictionary in the specified Save Path")
#     else:
#         self.status_text_string.set("Loading...")
#         self.text_status.config(fg="Red")
#         main_dictionary = {}
#         loaded_file = open(self.entry_Save_Path.get() + ('/index%s.txt' % ending), 'r').readlines()
#         for line in loaded_file:
#             if not line.__contains__('@'):
#                 line_split = line.split('~')
#                 term = line_split[0]
#                 term_index = line_split[1]
#                 term_tf = line_split[2]
#                 main_dictionary[term] = {'post_index': term_index,
#                                          'tf': term_tf}
#         if os.path.exists(self.entry_Save_Path.get() + '/parser_docs.txt'):
#             docs_dictionary = {}
#             doc_len_sum = 0
#             doc_count = 0
#             loaded_file = open(self.entry_Save_Path.get() + '/parser_docs.txt', 'r').readlines()
#             for line in loaded_file:
#                 if not line.__contains__('@'):
#                     line = line.replace('<', '').replace('>', '')
#                     line_split = line.split('~')
#                     doc = line_split[0]
#                     max_tf = line_split[1]
#                     max_term = line_split[2]
#                     num_of_terms = line_split[3]
#                     doc_city = line_split[4]
#                     doc_length = line_split[5]
#                     doc_entities = line_split[6]
#                     docs_dictionary[doc] = {'max_tf': max_tf,
#                                             'max_term': max_term,
#                                             'num_of_terms': num_of_terms,
#                                             'doc_city': doc_city,
#                                             'doc_length': doc_length,
#                                             'entities': doc_entities}
#                     doc_len_sum += int(doc_length)
#                     doc_count += 1
#             avgdl = float(doc_len_sum) / doc_count
#         if os.path.exists(self.entry_Save_Path.get() + '/languages.txt'):
#             self.language_list.delete(0, END)
#             loaded_languages_file = open(self.entry_Save_Path.get() + '/languages.txt', 'r').readlines()
#             for language in loaded_languages_file:
#                 if language != '':
#                     self.language_list.insert(END, language.replace('<', '').replace('>', ''))
#
#         self.status_text_string.set("Dictionary Loaded!")
#         self.text_status.config(fg="Blue")
#
#
# def city_filter(self):
#     if not os.path.exists(self.entry_Save_Path.get() + '/cities_index.txt'):
#         tkinter.messagebox.showerror("Error", "There is no cities dictionary in the specified Save Path")
#     else:
#         self.status_text_string.set("Loading...")
#         self.text_status.config(fg="Red")
#         loaded_file = open(self.entry_Save_Path.get() + '/cities_index.txt', 'r').readlines()
#         for line in loaded_file:
#             if not line == '':
#                 line_split = line.split('~')
#                 city = line_split[0]
#                 self.list_cities.add(city[1:len(city)])
#         city_window = Toplevel(root)
#         window_width = 200
#         window_height = 300
#         position_right = int(city_window.winfo_screenwidth() / 2 - window_width / 2)
#         position_down = int(city_window.winfo_screenheight() / 2 - window_height / 2)
#         city_window.geometry("200x300+{}+{}".format(position_right, position_down))
#         self.status_text_string.set("Working on cities...")
#         self.text_status.config(fg="Red")
#         ok_button = Button(city_window, text="Save", width="8", command=lambda: self.close_city_window(city_window,
#                                                                                                        checkboxes))
#         ok_button.pack()
#         scroll = Scrollbar(city_window, orient="vertical")
#         scroll.pack(side=RIGHT, fill=Y)
#         city_list = Text(city_window, width=30, height=17, yscrollcommand=scroll.set)
#         checkboxes = {}
#         checkbox_list = []
#         checkbox_var_list = []
#         city_list.pack(side=LEFT)
#         scroll.config(command=city_list.yview)
#
#         for city in sorted(self.list_cities):
#             var_city = IntVar()
#             cb = Checkbutton(city_window, text="%s" % city, variable=var_city, name=city.lower())
#             checkboxes[city] = var_city
#             checkbox_list.append(cb)
#             checkbox_var_list.append(var_city)
#             city_list.window_create("end", window=cb)
#             city_list.insert("end", "\n")
#
#
# def close_city_window(self, city_window, checkboxes):
#     self.city_into_query = ""
#     city_dictionary = {}
#     city_selected = False
#
#     for city in sorted(self.list_cities):
#         if checkboxes[city].get() == 1:
#             city_selected = True
#             city_dictionary[city] = 1
#
#             self.city_into_query += (city + " ")
#     if not city_selected:
#         for city in sorted(self.list_cities):
#             city_dictionary[city] = 1
#     self.status_text_string.set("Waiting for query...")
#     self.text_status.config(fg="Blue")
#     city_window.destroy()
#
#
# # this method return the dictionary that contain the query number and the information of every query
# def get_queries_from_doc(self):
#     queries_texts = {}
#     queries_file = open(self.entry_Queries_Path.get(), "r").read()
#     for query_contents in queries_file.split("</top>")[:-1]:
#         if query_contents != '\n':
#             query_number = query_contents.split('<title>')[0].split('Number: ')[1].replace(' ', '').replace('\n', '')
#         if '<title>' in query_contents:
#             query_text = query_contents.split('<title>')[1].split('<desc>')[0].replace('\n', ' ')
#         queries_texts[query_number] = {'query_number': query_number, 'query_text': query_text}
#     return queries_texts
#
#
# # this method saved all queries results to one file
# def save_query_results(self, query_number, docs):
#     queries_file_name = open(self.entry_Save_Path.get() + '/results.txt', "ab")
#     query_id = query_number.split(": ")[1]
#     # i = 1
#     # float_number = 1.0
#     for doc in docs:
#         queries_file_name.write(query_id + " 0 " + str(doc[0]) + ' 1 1.0 test\n')
#     tkinter.messagebox.showinfo("Done", "Query results saved!")
#
#
# def save_queries_results(self, queries_dic):
#     queries_file_name = open(self.entry_Save_Path.get() + '/results.txt', "ab")
#     for key in sorted(queries_dic.iterkeys()):
#         query_id = key
#         docs = queries_dic[key]
#         for doc in docs:
#             queries_file_name.write(query_id + " 0 " + str(doc) + ' 1 1.0 test\n')
#     tkinter.messagebox.showinfo("Done", "Queries results saved!")
#
#
# @staticmethod
# def doc_entities(doc_name):
#     global docs_dictionary
#     text_window = Toplevel(root)
#     window_width = 200
#     window_height = 200
#     position_right = int(text_window.winfo_screenwidth() / 2 - window_width / 2)
#     position_down = int(text_window.winfo_screenheight() / 2 - window_height / 2)
#     text_window.geometry("200x200+{}+{}".format(position_right, position_down))
#     exit_button = Button(text_window, text="Exit", command=lambda: text_window.destroy())
#     exit_button.pack()
#     doc_label = Label(text_window, text=("Doc Name: " + doc_name))
#     doc_label.pack(side="top", fill="both")
#     entities_label = Label(text_window, text='Top 5 Entities:')
#     entities_label.pack(side="top", fill="both")
#     entities = docs_dictionary[doc_name]['entities'].split(',')
#     for i in range(len(entities)):
#         label_text = str(i + 1) + ". " + (str(entities[i]).replace('\'', '').replace('[', '').replace(']', ''))
#         label_entity = Label(text_window, text=label_text)
#         label_entity.pack(side="top", fill="both")
