'''
Transform a downloaded PL grading spreadsheet into something usable.
'''
import pandas as pd
import json
import argparse



UID_SUFFIX = '@mail.gvsu.edu'

parser = argparse.ArgumentParser(description="Simplify PL grading CSV")
parser.add_argument("fname", help="CSV grading file downloaded from PL")
parser.add_argument("-g", "--group", action="store_true",
                    help="Grading a group assessment")
parser.add_argument('-u','--uids', nargs='*',
                    help='Optional list of uids without @... suffix '
                         '(defaults to selecting all)')
parser.add_argument('-q','--qids', nargs='*',
                    help='Optional list of qids '
                         '(defaults to selecting all)')
args = parser.parse_args()

dat = pd.read_csv(args.fname)

if args.group:
    num_cols_expected = 15
    desired_columns = ['group_name',
                       'uid_list',
                       'qid',
                       'submission_id',
                       'score_perc',
                       'feedback']
else:
    num_cols_expected = 15
    desired_columns = ['uid',
                       'qid',
                       'submission_id',
                       'score_perc',
                       'feedback']


# confirm that file has not already been modified
assert len(dat.columns) == num_cols_expected

dat = dat.get(desired_columns)

if args.uids is not None:
    # Note: if there are mixed suffixes and you don't want to type
    # them out manually, could instead easily use a regex match, though that
    # may result in false positives.  See:
    # https://stackoverflow.com/questions/17972938/
    # check-if-a-string-in-a-pandas-dataframe-column-is-in-a-list-of-strings

    full_desired_uids = set([u + UID_SUFFIX for u in args.uids])

    if args.group:
        # List of names is stored as string, which much be converted to list
        # using json. Then, find set intersection of that set with desired uids
        desired_rows = dat['uid_list'].apply(lambda r:
                        len(set(json.loads(r)) & full_desired_uids) > 0)
    else:
        desired_rows = dat['uid'].isin(full_desired_uids)

    dat = dat[desired_rows]

if args.qids is not None:
    desired_rows = dat['qid'].isin(args.qids)
    dat = dat[desired_rows]

dat.sort_values(by=dat.columns[0], inplace=True)

# Note: overwrites file with name fname
dat.to_csv(args.fname, index=False)
