// 전체 코드에 엄격 모드 적용
"use strict";

// Calculate의 결과 값
let result = null;


// Display 요소 선택
const display = document.getElementById('display');

// 숫자 버튼 선택
const numberButtons = document.querySelectorAll('.number-button');

// 숫자 버튼 클릭 이벤트 처리
numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.value; // 버튼의 value 값 가져오기
        display.value += value; // display에 값 추가
    });
});

// 초기화 버튼 처리
const clearButton = document.querySelector('.basic-button[id="AC"]');
clearButton.addEventListener('click', () => {
    display.value = ''; // display 초기화
    result = null;      // 연산 결과 초기화
});

// 삭제 버튼 처리
const deleteButton = document.querySelector('.basic-button[id="del"]');
deleteButton.addEventListener('click', () => {
    display.value = display.value.slice(0, -1); // 마지막 입력 삭제
});


