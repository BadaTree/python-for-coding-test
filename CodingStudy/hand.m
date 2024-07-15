% 파일명: hand_gesture_recognition.m

% 이미지 읽기
img = imread('hand_image.jpg');

% 그레이스케일 변환
grayImg = rgb2gray(img);

% 이진화
binaryImg = imbinarize(grayImg);

% 노이즈 제거
binaryImg = medfilt2(binaryImg);

% 윤곽선 검출
contours = bwboundaries(binaryImg);

% 가장 큰 윤곽선 선택
[~, idx] = max(cellfun(@length, contours));
handContour = contours{idx];

% 볼록 껍질 구하기
k = convhull(handContour(:, 1), handContour(:, 2));

% 손가락 끝 찾기 (볼록 껍질에서 윤곽선과의 차이로)
defects = findDefects(handContour, k);

% 손가락 개수 세기
numFingers = length(defects);

% 손가락 개수에 따른 분류
if numFingers == 1
    disp('1');
elseif numFingers == 2
    disp('2');
elseif numFingers == 3
    disp('3');
elseif numFingers == 4
    disp('4');
elseif numFingers == 5
    disp('5');
else
    disp('Unknown');
end

function defects = findDefects(handContour, k)
    % 손가락 끝을 찾기 위한 사용자 정의 함수
    defects = [];
    for i = 1:length(k)
        % 볼록 껍질의 점과 윤곽선의 점 사이의 차이 계산
        if someCondition(handContour, k, i)
            defects = [defects; k(i)];
        end
    end
end

function result = someCondition(handContour, k, i)
    % 손가락 끝을 감지하기 위한 조건을 정의하는 함수
    % 여기서는 단순히 임의의 조건을 사용합니다. 실제로는 손가락 끝을 감지할 수 있는 적절한 논리를 구현해야 합니다.
    result = true;  % 예시 조건, 실제로는 더 복잡한 논리가 필요
end
