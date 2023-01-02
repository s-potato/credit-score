debtloan = float(input("Number of Debt Consolidation Loan? "))
changed_credit = float(input("Percentage change in credit card limit? "))
annual_income = float(input("Your Annual Income? "))
numloan = float(input("Number of Loan? "))
creditage = float(input("How old are your credit? "))
delaypayment = float(input("Number of Delayed Payment? "))
numbank = float(input("Number of Bank Accounts? "))
daysdelay = float(input("Average number of days delayed from the payment date? "))
numinquiries = float(input("Number of Inquiries? "))
numcard = float(input("Number of Credit Card? "))
outdebt = float(input("Your Outstanding Debt? "))
inte_rate = float(input("Interest_Rate?"))
print("Credit Mix:\n\t0. Bad\n\t1. Standard\n\t2. Good")
credit_mix = int(input("> "))
while credit_mix not in [0, 1, 2]:
    credit_mix = int(input("Please select from above list: "))

data = [debtloan, changed_credit, annual_income,
    numloan, creditage, delaypayment, numbank,
    daysdelay, numinquiries, numcard,
    outdebt, inte_rate, credit_mix]

def get_decision_path(clf, X_test):
    n_nodes = clf.tree_.node_count
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    feature = clf.tree_.feature
    threshold = clf.tree_.threshold
    node_indicator = clf.decision_path(X_test)
    leaf_id = clf.apply(X_test)
    classes = clf.predict(X_test)

    for sample_id in range(0, len(X_test)):
        node_index = node_indicator.indices[
            node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
        ]

        print("Rules used to predict sample {id}:\n".format(id=sample_id))
        for node_id in node_index:
            # continue to the next node if it is a leaf node
            if leaf_id[sample_id] == node_id:
                continue

            # check if value of the split feature for sample 0 is below threshold
            if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
                threshold_sign = "<="
            else:
                threshold_sign = ">"

            print(
                "decision node {node} : (X_test[{sample}, {feature}] = {value}) "
                "{inequality} {threshold})".format(
                    node=node_id,
                    sample=sample_id,
                    feature=clf.features[feature[node_id]],
                    value=X_test[sample_id, feature[node_id]],
                    inequality=threshold_sign,
                    threshold=threshold[node_id],
                )
            )
        print(f'Sample {sample_id} is {clf.labels[classes[sample_id]]}')
        print("*"*50)
        print()

import pickle
import numpy as np

X = np.array([data])

filename = 'model.pkl'
with open(filename, 'rb') as file:
    clf = pickle.load(file)

get_decision_path(clf, X)