from rest_framework import serializers

from .models import Article, Comment

class AritcleListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    # 직렬화 하고자 하는 필드를 지정
    fields = (
      'id',
      'title',
      'content',
    )

class ArticleSerializer(serializers.ModelSerializer):
  # 게시글에 해당하는 댓글, 왜 AritcleSerializer 안에 중첩으로 있을까?
  # CommentDeailSerializer는 반드시 ArticleSerializer안에서만 사용되기 때문이다. 
  class commentDetailSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields= (
        'id',
        'content',
      )
  # 필드 2개 추가 : 읽기 전용 필드 설정 
  # 1.사용자로부터 입력 받지 않는다.
  # 2. 유효성 검사 과정에서 제외된다.
  # 3. 결과 데이터는 포함되어 클라이언트에 제공된다.

  comment_set = commentDetailSerializer(many=True, read_only = True)
  # comment_set : 역참조, count : 메서드
  comment_count = serializers.IntegerField(
    source = 'comment_set.count', read_only=True
  )
  class Meta:
    model = Article
    # __all__ 모든 필드 직렬화
    fields = '__all__'


class CommmentSerializer(serializers.ModelSerializer):
  # 댓글을 조회했을때 게시글의 제목도 같이 나오게
  class AritlceTitleSerializer(serializers.ModelSerializer):
    class Meta:
      model = Article
      fields = ('title',)
  # 댓글을 조회했을 때 같이 나오는 게시글의 제목은 읽기 전용 
  article = AritlceTitleSerializer(read_only=True)
  class Meta:
    model = Comment
    fields = '__all__'