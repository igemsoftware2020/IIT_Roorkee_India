from django.db import models


class Job(models.Model):

    """
    Each "Job" consists of an id, name of bacteria, email id, and status of job
    """

    # choices for bacteria
    BACTERIA_1 = 'acinetobacter baumannii'
    BACTERIA_2 = 'B2'
    BACTERIA_3 = 'B2'
    BACTERIA_CHOICES = [
        (BACTERIA_1, 'Bacteria_1'),
        (BACTERIA_2, 'Bacteria_2'),
        (BACTERIA_3, 'Bacteria_3'),
    ]

    # choices for status
    STEP_1 = 'S1'
    STEP_2 = 'S2'
    STEP_3 = 'S3'
    STATUS_CHOICES = [
        (STEP_1, 'Step_1'),
        (STEP_2, 'Step_2'),
        (STEP_3, 'Step_3'),
    ]

    bacteria = models.CharField(
        max_length=256,
        choices=BACTERIA_CHOICES,
        blank=False,
        null=False
    )

    email_id = models.EmailField(
        max_length=254, blank=False, null=False
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=STEP_1,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return f"""{self.id} - {self.bacteria}"""

    def get_absolute_url(self):
        return reverse("Job_detail", kwargs={"pk": self.pk})
