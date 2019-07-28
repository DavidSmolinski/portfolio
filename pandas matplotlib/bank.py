import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('bank.csv', delimiter=';')
print('''I'm changing column data types to make the dataframe (df) small and fast.\n\nold df properties:\n''')
df.info(memory_usage='deep')
old_df_size = df.memory_usage(deep=True).sum()

df = pd.read_csv('bank.csv', delimiter=';',
                 dtype={'job': 'category', 'marital': 'category',
                        'month': 'category', 'contact': 'category', 'poutcome': 'category'})
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', 200)
df.education = pd.Categorical(df.education, categories=["primary", "secondary", "tertiary", "unknown"], ordered=True)
for e in ('default', 'housing', 'loan', 'y'):
    df[e] = df[e].str.contains('yes').astype(int)

print('\nnew df:\n')
df.info(memory_usage='deep')
new_df_size = df.memory_usage(deep=True).sum()
print(f'\nmemory saved: {old_df_size - new_df_size} B\n')
print(df.head(2))

# Education vs Balance bar graph
plt.xlabel('education')
plt.ylabel(r'account balance ($)')
plt.title('Education vs Account Balance')
plt.bar(df.education, df.balance)
plt.savefig('ed bal.png')
# plt.show()


# Age vs Balance scatter plot, histograms for age and balance
# make subplot axes
ax_scatter = plt.subplot2grid(shape=(4, 4), loc=(1, 0), rowspan=3, colspan=3)  # scatter plot
ax_histx = plt.subplot2grid(shape=(4, 4), loc=(0, 0), rowspan=1, colspan=3)  # histogram for x axis
ax_histy = plt.subplot2grid(shape=(4, 4), loc=(1, 3), rowspan=3, colspan=1)  # histogram for y axis

ax_scatter.tick_params(direction='in', top=True, right=True)
ax_histx.tick_params(direction='in', labelbottom=False)
ax_histy.tick_params(direction='in', labelleft=False)

# make plots
ax_scatter.scatter(df.age, df.balance)
ax_histx.hist(df.age, bins=40)
ax_histy.hist(df.balance, bins=40, orientation='horizontal')

age_min, age_max = df.age.min(), df.age.max()
ax_scatter.set_xlim((age_min, age_max))
ax_scatter.set_ylim((df.balance.min(), df.balance.max()))
ax_histx.set_xlim(ax_scatter.get_xlim())
ax_histy.set_ylim(ax_scatter.get_ylim())

ax_scatter.set_xlabel('age of client')
ax_scatter.set_ylabel(r'account balance ($)')
ax_histx.set_ylabel('frequency\nof age\ngroups')
ax_histy.set_xlabel('frequency of\nacc. bal. groups')

plt.tight_layout()
plt.savefig('age bal.png')
# plt.show()


# Age vs Balance box plot without outliers
balance_series_list = []
age_labels = []

for age in range(age_min, age_max + 1):
    balance_ser = df.loc[df.age == age, 'balance']
    if not balance_ser.empty:
        balance_series_list += [balance_ser]
        age_labels += [age]

fig1, ax1 = plt.subplots()
ax1.boxplot(balance_series_list, showfliers=False)
ax1.set_xticklabels(labels=age_labels, fontsize=4)
ax1.set_xlabel('ages')
ax1.set_ylabel('balance ($)')
ax1.set_title('Age vs Balance')
fig1.savefig('age bal box.png', dpi=300)
# plt.show()


# Unknown Education vs Balance box plot without outliers
balance_ser2 = df.loc[df.education == 'unknown', 'balance']
fig2, ax2 = plt.subplots()
ax2.boxplot([balance_ser2], showfliers=False)
ax2.set_xticklabels(labels=['unknown'])
ax2.set_xlabel('education')
ax2.set_ylabel('account balance ($)')
ax2.set_title('Unknown Education vs Account Balance')
fig2.savefig('unk ed bal.png')
# plt.show()
