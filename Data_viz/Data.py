#-----Bar Plot-----
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="darkgrid", color_codes=True)

# titanic=sns.load_dataset("titanic")
# sns.catplot(x="sex",y="survived",hue="class",kind="bar",data=titanic)
# plt.show()

#-----Count Plot-----
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes=True)
# titanic=sns.load_dataset("titanic")
# print(titanic)
# p1=sns.countplot(x="sex" ,hue="class",data=titanic)
# plt.show() 


#-----Scatter Plot-----
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes=True)
# titanic=sns.load_dataset("titanic")
# g=sns.FacetGrid(titanic,row="sex",hue="alone")
# g=(g.map(plt.scatter,"age","fare").add_legend())
# plt.show()

 