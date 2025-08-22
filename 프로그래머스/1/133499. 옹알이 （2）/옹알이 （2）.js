const originalWords = [
    {
        index: 0,
        word: "aya"
    },
    {
        index: 1,
        word: "ye",
    },
    {
        index: 2,
        word: "woo",
    },
    {
        index: 3,
        word: "ma",
    },
];

const checkWord = (str, words) => {
    if (str.length === 0) {
        return true;
    }
    for (let i = 0; i < words.length; i++) {
        const currentWord = words[i];
        if (str.startsWith(currentWord.word)) {
            return checkWord(str.slice(currentWord.word.length), originalWords.filter((word) => word.index !== currentWord.index));
        }
    }

    return false;
}

function solution(babbling) {
    return babbling.reduce((acc, cur) => {
        if (checkWord(cur, originalWords)) {
            acc += 1
        }

        return acc;
    }, 0)
}