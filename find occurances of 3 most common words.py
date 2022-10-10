
list=['lock','key','gate','lock','lock','gate','mat']
def function(list):
    counts = dict()
    for i in list:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    print ({k: v for k, v in sorted(counts.items(), key=lambda item: item[1],reverse=True)})
    return counts

function(list)

