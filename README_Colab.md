### How to access google colab
- You can https://colab.research.google.com/

### How to open case studies notebooks from Great Learning into colab
- Go to your weekly course content and find the Session Notebook within GreatLearning platform
- Once you open the Session notebook, you will see an option to download it.
- After you download, you can upload it inside your google colab

### How to load data into google colab
- If you have csv files in your google drive:
  - you can mount your google drive and access your files
  - For example, we have a folder in MyDrive called greatlearning which has 3 csv files
  - You first have to mount your drive using following two commands:
    - ```from google.colab import drive```
    - ```drive.mount('/content/drive')```
  - This will prompt for permissions to access to your Google Drive
  - Once you authorize, you will see a new directory in folders inside your colab called ```drive```
  - Now you can go into the drive and see that it will have all content from your drive.
  - Let say you have a csv file called movie.csv in drive/MyDrive/greatlearning directory.
  - You will have to run the below command to load it:
    - ```movie = pd.read_csv("drive/MyDrive/greatlearning/movie.csv")```
  - With the above command, you now have loaded the entire csv in variable called ```movie```
  - You can run the list command to see other content in your drive like linux style using following command:
    - ```!ls drive/MyDrive```

### How to install pandas and numpy
  - ```pip install pandas```
  - ```pip install numpy```

### How to upload a file from local machine

- You can upload a file from local machine to your colab notebook file storage using upload option in there.
- You can then simply refer to it in your code like below:

```
file_path = '/content/foodhub_order.csv'
df = pd.read_csv(file_path)
```

## How to convert ipynb to html
1. Download your notebook as .ipynb file to your local machine
2. Open the Google Colab with any existing notebook or empty notebook
3. Upload the downloaded .ipynb file to the online File storage of your Google Colab notebook
4. Run the below statements in your code element in your Google Colab notebook:

    ```
    %%shell
    jupyter nbconvert --to html /content/YOUR_NOTE_BOOK_NAME.ipynb
    ```