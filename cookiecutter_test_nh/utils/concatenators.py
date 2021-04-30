def concat_cols(df, col_list):
    """concatenate columns in a dataframe

    Args:
        dataframe
        column names to concatenate
    """
    concat = df[col_list[0]]
    for i in range(1, len(col_list)):
        concat = concat + " " + df[col_list[i]]
        return concat


def concat_rows(df, groupby_col, concat_col):
    """concatenate rows in a dataframe

    Args:
        dataframe
        column to groupby
        column with rows to concatenate
    """
    row_concat = (
        df.groupby([groupby_col])[concat_col].apply(lambda x: " ".join(x)).reset_index()
    )
    return row_concat
