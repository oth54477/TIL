const solution = (clothes) => 
  Object.values(clothes.reduce((counts, [, type]) => (counts[type] = (counts[type] || 0) + 1, counts), {}))
    .reduce((product, count) => product * (count + 1), 1) - 1;