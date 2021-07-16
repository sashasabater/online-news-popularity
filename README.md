# Predicting Online News Popularity 
## Using features known before publication, can one predict how many shares an online article will have once published? 
The ability to predict popularity would be an invaluable tool in today's economy of online influence. Our newsfeeds are dictated by what algorithms think we want to see, but they are also dictated by what's popular amongst our own social networks. Being able to not only signify what features in an online news article are impactful for numbers of shares, but to also predict the number of shares would be influential in its own right. By using regression machine learning models, I attempt to do just that. 

## Data 
This dataset was donated to the UCI Machine Learning Repository and can be accessed [here](https://archive.ics.uci.edu/ml/datasets/Online+News+Popularity). It consists of data for about 39,000 news articles all scraped from the online news website [Mashable](https://mashable.com/). Additionally it includes the total number of shares across various social media platforms for each article. This dataset also contains features engineered by its compilers, whose published paper detailing data acquisition and feature meanings can be found [here](https://repositorium.sdum.uminho.pt/bitstream/1822/39169/1/main.pdf). 

## EDA 
Upon data exploraton, I noticed quite a range of numbers of shares, from 1 to more than 800,000.
![Shares_EDA]('./img/eda-outlier.png')

With a mean of about 3000, and a standard deviation of more than 11,000, I figured that there must be a number of outliers that I should handle before trying to fit any models. 
![Outliers]('./img/outliers.png')
