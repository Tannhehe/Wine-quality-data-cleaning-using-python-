In the Task 1 , I have worked on the wine quality dataset ( from kaggle ) . First , I imported all the necessary libraries such as pandas , numpy , seaborn , matplotlib . 
I loaded the dataset and checked it's structure , data type and also whether there were any missing values . There were no missing values . 
Then , I created a Boxplot to identify the outliers. I used the IQR ( Interquartile Range ) method to remove those outliers from each column ( except the "quality" column to make the data cleaner and more reliable .
After cleaning , I have scaled the data using StandardScaler so that all the values are on similar scale ( helps in better model performance ).
I have also generated a Heatmap to visualise the correaltion between different features and understand which ones are more related to wine quality .
Overall, this task was focused on data cleaning, outlier removal, scaling and visualizing relationships between variables.
