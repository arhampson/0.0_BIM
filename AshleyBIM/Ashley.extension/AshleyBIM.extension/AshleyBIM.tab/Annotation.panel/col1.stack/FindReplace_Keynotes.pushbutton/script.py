import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
import os
import re
import sys
from System.Windows.Forms import Application, Form, Label, Button, TextBox, OpenFileDialog, ListBox, MessageBox
from System.Drawing import Point

class SimpleFileSearchForm(Form):
    def __init__(self):
        self.Text = "Keynotes Find/Replace"
        self.Width = 400
        self.Height = 270

        self.browse_button = Button()
        self.browse_button.Text = "Browse"
        self.browse_button.Location = Point(20, 20)
        self.browse_button.Click += self.browse_button_clicked
        self.Controls.Add(self.browse_button)

        self.selected_file_label = Label()
        self.selected_file_label.Text = "Selected File: None"
        self.selected_file_label.Location = Point(20, 50)
        self.selected_file_label.Height = 40
        self.Controls.Add(self.selected_file_label)

        self.label = Label()
        self.label.Text = "Enter word to find:"
        self.label.Location = Point(20, 90)
        self.label.Width = 150
        self.Controls.Add(self.label)

        self.search_box = TextBox()
        self.search_box.Location = Point(170, 90)
        self.search_box.Width = 150
        self.Controls.Add(self.search_box)

        self.search_button = Button()
        self.search_button.Text = "Find"
        self.search_button.Location = Point(20, 120)
        self.search_button.Click += self.search_button_clicked
        self.Controls.Add(self.search_button)

    def browse_button_clicked(self, sender, event):
        dialog = OpenFileDialog()
        dialog.Filter = "Text Files|*.txt"
        result = dialog.ShowDialog()
        if result.ToString() == "OK":
            file_path = dialog.FileName
            file_name = os.path.basename(file_path)
            self.selected_file_label.Text = "Selected File: " + file_name
            self.file_path = file_path

    def search_button_clicked(self, sender, event):
        if not hasattr(self, 'file_path'):
            MessageBox.Show("Please select a file before searching.")
        elif not self.search_box.Text:
            MessageBox.Show("Please enter a word to search.")
        else:
            search_word = self.search_box.Text
            with open(self.file_path, 'r') as file:
                content = file.read()
                matches = re.findall(r'\b{}\b'.format(search_word), content, re.IGNORECASE)
                if not matches:
                    MessageBox.Show("No matches found.")
                else:
                    result_form = SearchResultsForm(matches, search_word, self.file_path)
                    result_form.ShowDialog()

class SearchResultsForm(Form):
    def __init__(self, matches, search_word, file_path):
        self.Text = "Search Results"
        self.Width = 400
        self.Height = 500
        self.matches = matches
        self.search_word = search_word
        self.file_path = file_path

        self.browse_button = Button()
        self.browse_button.Text = "Browse"
        self.browse_button.Location = Point(20, 20)
        self.browse_button.Click += self.browse_button_clicked
        self.Controls.Add(self.browse_button)

        self.selected_file_label = Label()
        self.selected_file_label.Text = "Selected File: " + os.path.basename(self.file_path) if self.file_path else "Selected File: None"
        self.selected_file_label.Location = Point(20, 60)
        self.selected_file_label.Height = 40
        self.Controls.Add(self.selected_file_label)

        if not self.matches:
            self.result_label = Label()
            self.result_label.Text = "No matches found."
            self.result_label.Location = Point(20, 100)
            self.Controls.Add(self.result_label)
        else:
            self.result_label = Label()
            self.result_label.Text = "Search Results for '" + self.search_word + "':"
            self.result_label.Location = Point(20, 100)
            self.Controls.Add(self.result_label)

            self.results_listbox = ListBox()
            self.results_listbox.Location = Point(20, 130)
            self.results_listbox.Width = 250
            self.results_listbox.Height = 200
            for match in self.matches:
                self.results_listbox.Items.Add(match)
            self.Controls.Add(self.results_listbox)

            self.replace_label = Label()
            self.replace_label.Text = "Replace:"
            self.replace_label.Location = Point(20, 340)
            self.Controls.Add(self.replace_label)

            self.replace_box = TextBox()
            self.replace_box.Location = Point(130, 340)
            self.replace_box.Width = 150
            self.Controls.Add(self.replace_box)

            self.replace_button = Button()
            self.replace_button.Text = "Replace"
            self.replace_button.Location = Point(20, 370)
            self.replace_button.Click += self.replace_button_clicked
            self.Controls.Add(self.replace_button)

    def browse_button_clicked(self, sender, event):
        dialog = OpenFileDialog()
        dialog.Filter = "Text Files|*.txt"
        result = dialog.ShowDialog()
        if result.ToString() == "OK":
            file_path = dialog.FileName
            file_name = os.path.basename(file_path)
            self.selected_file_label.Text = "Selected File: " + file_name
            self.file_path = file_path

    def replace_button_clicked(self, sender, event):
        replace_word = self.replace_box.Text
        with open(self.file_path, 'r') as file:
            file_content = file.read()
            new_content, count = re.subn(r'\b{}\b'.format(self.search_word), replace_word, file_content, flags=re.IGNORECASE)
        with open(self.file_path, 'w') as file:
            file.write(new_content)
        MessageBox.Show(str(count) + " occurrences replaced.")
        self.Close()

if __name__ == "__main__":
    form = SimpleFileSearchForm()
    Application.Run(form)
