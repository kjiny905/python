// 함수 선언문
function add(x, y) {
  return x + y;
}

// 함수 표현식
const add2 = function (x, y) {
  return x + y;
};

// 화살표 함수
// const add3 = (x, y) =>{
//   return x + y;
// }
// 생략 사용
const add3 = (x, y) => x + y;

const result = add(10, 20);
const result2 = add2(10, 20);
const result3 = add3(10, 20);

console.log(result, result2, result3);

// 고차함수
{
  const arr = [1, 2, 3];

  const f2 = x => 2 * x;
  const f3 = x => 3 * x;

  function multiply2(arr, f) {
    const result10 = [];
    for (let i = 0; i < arr.length; i++) {
      result10[i] = f(arr[i]);
    }
    return result10;
  }
  console.log(multiply2(arr, f2));
  console.log(multiply2(arr, f3));
  console.log(multiply2(arr, x => 4 * x));
}
