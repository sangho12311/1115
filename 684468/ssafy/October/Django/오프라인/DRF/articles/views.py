from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
from .models import Article, Comment
from .serializers import (
    AritcleListSerializer,
    ArticleSerializer,
    CommmentSerializer,
)

# list : 전체 객체 조회, 객체가 하나도 없다 ---> 404예외 발생
# object : 단일 객체 조회, 객체가 없으면 ---> 404예외 발생
# 4xx : 클라이언트 에러
# 5xx : 서버 에러
# 404 : Not found
from django.shortcuts import get_object_or_404, get_list_or_404


# GET요청 : 전체 게시글 조회
# POST요청 : 새 게시글 생성
@api_view(['GET', 'POST'])
def article_list(request):
  if request.method == 'GET':
    articles = get_list_or_404(Article)
    # 모든게시글을 DB에서 가져오고 ---> 직렬화(우리가 필요한건 json 데이터)
    # 여러개의 객체(다중 데이터)일때 many=True
    serializer = AritcleListSerializer(articles, many=True)
    # 직렬화된 데이터를 json형식으로 응답
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ArticleSerializer(data=request.data) # 직렬화
    # raise_exception=True ---> 유효하지 않을경우 예외 발생 
    if serializer.is_valid(raise_exception=True):# 유효성 검사
      serializer.save()
      # 데이터 생성 성공/실패 // 성공:HTTP_201, 실패:HTTP_400
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    # 데이터 생성 실패 했을 때 상태 코드 HTTP_400_BAD_REQUEST로 응답
    # raise_exception=True 때문에 주석처리
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
  # 단일 게시글 DB에서 조회
  article = get_object_or_404(Article, pk=article_pk)
  if request.method == 'GET': # 단일 게시글 조회
    # 직렬화 ---> 응답
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

  elif request.method == "DELETE": # 게시글 삭제
    article.delete()
    # 상태 코드 HTTP_204 : 요청 성공, 반환할 콘텐츠가 없음
    return Response(status=status.HTTP_204_NO_CONTENT)

  elif request.method == "PUT": # 게시글 수정
    # 기존 게시글을 요청(data=request.data)해서 ---> 수정
    # partial=True : 부분 업데이트 허용(일부 필드만 수정 가능)
    serializer = ArticleSerializer(
      article, data=request.data, partial=True
    )
    # raise_exception=True : 유효하지 않을 경우 ---> 예외 발생
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    
    # raise_exception=True 때문에 주석 처리
    # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request):
  comments = get_list_or_404(Comment)
  #직렬화
  serializer = CommmentSerializer(comments, many=True)
  return Response(serializer.data)

# 댓글 상세페이지 --> 조회, 수정, 삭제 가능하다. 
@api_view(['GET','DELETE','PUT'])
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
      #직렬화 --> 응답
      serializer = CommmentSerializer(comment)
      return Response(serializer.data)
    
    elif request.method == 'DELETE':
      comment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
      serializer = CommmentSerializer(comment, data=request.data)
      # 유효성 검사
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
@api_view(['POST'])
def comment_create(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  serializer = CommmentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    # article과 comment는 1:N관계(comment에 article의 외래키)
    serializer.save(article=article)
    return Response(serializer.data, status=status.HTTP_201_CREATED)