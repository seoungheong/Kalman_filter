#평균 필터(Average Filter)

## 재귀식(Recurrence relating) ??
> 이전 결과를 다시 활용하는 식, 결과를 재사용하기에 계산 효율이 좋다

## 평균의 재귀식
require('mathjax').init({
  loader: {load: ['input/tex', 'output/svg']}
}).then((MathJax) => {
  const svg = MathJax.tex2svg('\\frac{1}{x^2-1}', {display: true});
  console.log(MathJax.startup.adaptor.outerHTML(svg));
}).catch((err) => console.log(err.message));
