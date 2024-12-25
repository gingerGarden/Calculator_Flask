// 전체 코드에 엄격 모드 적용
"use strict";


// 화살표 버튼 기능 추가



// 키보드 입력 처리
document.addEventListener('keydown', (event) => {
    const key = event.key; // 눌린 키 값을 가져옴

    // 숫자 입력 처리 (0-9)
    if (!isNaN(key)) {
        display.value += key;
    }

    // 백스페이스 키 처리
    if (key === 'Backspace') {
        display.value = display.value.slice(0, -1); // 마지막 입력 삭제
    }

    // 초기화 키 (Escape) 처리
    if (key === 'Escape') {
        display.value = ''; // display 초기화
        result = null;      // 연산  결과 초기화
    }

    // 허용되지 않은 키 방지
    if (!['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Backspace', 'Escape', 'Enter'].includes(key)) {
        event.preventDefault(); // 불필요한 키 입력 방지
    }

    // // Enter 키 처리 (추후 계산 기능 추가 가능)
    // if (key === 'Enter') {
    //     console.log('Enter key pressed: Calculation could be triggered here');
    // }
});