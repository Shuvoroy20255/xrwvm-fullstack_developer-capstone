def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(pk=submission_id)
    choices = submission.choices.all()
    
    total_score = 0
    possible_score = 0
    selected_ids = []
    
    for choice in choices:
        selected_ids.append(choice.id)
        possible_score += choice.question.grade
        if choice.is_correct:
            total_score += choice.question.grade
    
    passed = total_score >= possible_score * 0.5
    
    context = {
        'course': course,
        'submission': submission,
        'choices': choices,
        'total_score': total_score,
        'possible_score': possible_score,
        'selected_ids': selected_ids,
        'passed': passed,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
