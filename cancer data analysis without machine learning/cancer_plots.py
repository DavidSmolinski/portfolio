import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('dataR2.csv', delimiter=',')
pd.set_option('display.max_columns', None)
df = df.rename(columns={'Classification': 'has_cancer'})

print(df.head(1))

header = df.columns.values.tolist()
healthy = 1
has_cancer = 2


def box_plots_for_all_vars(show_not_save=True):
    """has_cancer (cancer + and -) box plots for each variable
        :param show_not_save: if False, save as .png
    """
    for y in header[0:-1]:
        plt.boxplot([df.loc[df.has_cancer == healthy, y], df.loc[df.has_cancer == has_cancer, y]], showfliers=True,
                    widths=.9)
        plt.xticks([1, 2], ['healthy', 'cancer patient'])
        plt.title(f'Cancer vs {y}')
        plt.ylabel(y)
        if show_not_save is True:
            plt.show()
        else:
            plt.savefig(f'Cancer vs {y} Box Plot.png')
        plt.clf()


def one_box_plot_for_all_vars():
    """Print one fig with cancer + and - box plots for each variable"""
    loc_lists2 = []
    xticks_list = []
    for y in header[0:-1]:
        loc_lists = [df.loc[df.has_cancer == healthy, y], df.loc[df.has_cancer == has_cancer, y]]
        loc_lists2 += loc_lists
        xticks_list += [f'{y}-', f'{y}+']

    plt.boxplot(loc_lists2, showfliers=False, widths=.9)
    plt.title('Box Plots For All Cancer Variables')
    plt.xlabel('variable, "+" means cancer')
    plt.xticks(list(range(1, len(xticks_list) + 1)), xticks_list)
    plt.show()
    plt.clf()


def cancer_hist(var,show_not_save=True):
    """a histogram for cancer + and - for var
    :param var: string, the df column other than has_cancer
    """
    plt.hist(df.loc[df.has_cancer == healthy, var], alpha=.5, bins=9, label='healthy')
    plt.hist(df.loc[df.has_cancer == has_cancer, var], alpha=.5, bins=9, label='cancer')
    plt.legend()
    plt.xlabel(var)
    plt.ylabel('people')
    plt.title(f'{var} and cancer')
    if show_not_save is True:
        plt.show()
    else:
        plt.savefig(f'{var} and cancer.png')
    plt.clf()


def describe_var(var):
    """prints pandas describe() for cancer + and - for var
    :param var: string, the df column other than has_cancer
    """
    var_cancer = df.loc[df.has_cancer == has_cancer, var].describe()
    print(f'\n{var} cancer+\n{var_cancer}')
    var_healthy = df.loc[df.has_cancer == healthy, var].describe()
    print(f'\n{var} cancer-\n{var_healthy}')


describe_var('Age')
box_plots_for_all_vars(show_not_save=False)
one_box_plot_for_all_vars()
cancer_hist()

cancer_hist(var='Age',show_not_save=False)
cancer_hist('Glucose',False)

threshold=120
threshold_ratio = df.loc[df.has_cancer == has_cancer, 'Glucose']
threshold_ratio = df.loc[(df.has_cancer == has_cancer) & (df.Glucose > threshold), 'Glucose'].sum() / df.loc[df.has_cancer == has_cancer, 'Glucose'].sum()
print(f'\nThe glucose threshold of > {threshold} captures {threshold_ratio * 100}% of cancer +.')
