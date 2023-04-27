from django.db import models
from django.contrib.auth.models import User

AVS_Outcome = [
    ('Pass','Pass'),
    ('Fail','Fail'),
]

The_QA_Outcome = [
    ('Zero-defect','Zero-defect'),
    ('Defective','Defective'),
    ('Refer to Commit','Refer to Commit'),
]

The_QAC_Correction = [
    ('True','True'),
    ('False','False'),
]

KPA_Outcome = [
    ('Product','Product'),
    ('Pass','Pass'),
    ('Compliance','Compliance'),
    ('Data Capturing','Data Capturing'),
    ('TCF','TCF'),
    ('Underwriting','Underwriting'),

]

date_of_debit = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20'),
    ('21','21'),
    ('22','22'),
    ('23','23'),
    ('24','24'),
    ('25','25'),
    ('26','26'),
    ('27','27'),
    ('28','28'),
    ('29','29'),
    ('30','30'),
    ('31','31'),    
]

date_of_start = [
    ('1st_Jan','1st of January'),
    ('1st_Feb','1st of February'),
    ('1st_Mar','1st of March'),
    ('1st_Apr','1st of April'),
    ('1st_May','1st of May'),
    ('1st_June','1st of June'),
    ('1st_July','1st of July'),
    ('1st_Aug','1st of August'),
    ('1st_Sept','1st of September'),
    ('1st_Oct','1st of October'),
    ('1st_Nov','1st of November'),
    ('1st_Dec','1st of December'),

]

# Create your models here.
class QAAudit(models.Model):
    AuditDate = models.DateTimeField(auto_now_add=True)
    QA_Audit = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    CaseNumber = models.IntegerField(null=False, )
    PolicyNumber = models.CharField(max_length=12,null=False ,)
    AVS = models.CharField(choices=AVS_Outcome,null=False , max_length=5)
    debit_date = models.CharField(choices=date_of_debit,null=False ,max_length=20)
    start_date = models.CharField(choices=date_of_start,null=False ,max_length=20)
    sales_date = models.CharField(max_length=30, null=False )
    Caller_id = models.CharField(max_length=50, null=False )
    Cover_amount = models.CharField(max_length=13, null=False )
    Premium = models.CharField(max_length=10, null=False )
    Duration = models.CharField(max_length=6, null=False, default=0)
    QA_Outcome = models.CharField(choices=The_QA_Outcome,null=False ,max_length=20)
    QAC_Correction = models.CharField(choices=The_QAC_Correction, max_length=5, null=False ,)
    KPA = models.CharField(choices=KPA_Outcome, max_length=50, null=False)
    KPA_1 = models.CharField(choices=KPA_Outcome, max_length=50, null=True)
    KPA_2 = models.CharField(choices=KPA_Outcome, max_length=50, null=True)
    KPA_3 = models.CharField(choices=KPA_Outcome, max_length=50, null=True)
    Comment = models.TextField(max_length=200, null=False)
    Sales_agent = models.CharField(max_length=50, null=False)

    
    def __str__(self):
        return self.PolicyNumber
