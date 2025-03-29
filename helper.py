def fetch_stats(Selected_user , df ):

    if Selected_user == 'Overall':
        return df.shape[0]
    else:
        return df[df['user'] == Selected_user].shape[0]