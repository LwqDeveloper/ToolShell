## Xcode 快捷代码

### block  ppb
/// <#summary#>
@property (nonatomic, copy  ) void(^<#name#>)(<#Title#> *<#name#>);

### ppa
/// <#summary#>
@property (nonatomic, assign) <#Title#> <#name#>;

### ppc
/// <#summary#>
@property (nonatomic, copy  ) <#Title#> *<#name#>;

### pps
/// <#summary#>
@property (nonatomic, strong) <#Title#> *<#name#>;

### ppw
/// <#summary#>
@property (nonatomic, weak  ) <#Title#> *<#name#>;

### pplog
NSLog(@"%@", <#content#>);

### property ppg
- (<#NSObjec#> *)<#name#> {
    if (!_<#name#>) {
        _<#name#> = [[<#NSObject#> alloc] init];
    }
    return _<#name#>;
}

### pplabel 快捷label
- (UILabel *)<#nameLbl#> {
    if (!_<#nameLbl#>) {
        _<#nameLbl#> = [[UILabel alloc] init];
        _<#nameLbl#>.font = <#font#>;
        _<#nameLbl#>.textColor = <#color#>;
    }
    return _<#nameLbl#>;
}

### ppbutton 快捷button
- (UIButton *)<#button#> {
    if (!_<#button#>) {
        _<#button#> = [UIButton buttonWithType:UIButtonTypeCustom];
        _<#button#>.titleLabel.font = <#font#>;
        [_<#button#> setTitle:@"<#title#>" forState:UIControlStateNormal];
        [_<#button#> setTitleColor:<#color#> forState:UIControlStateNormal];
        [_<#button#> addTarget:self action:@selector(<#selector#>) forControlEvents:UIControlEventTouchUpInside];
    }
    return _<#button#>;
}

### ppimageview 快捷imageview
- (UIImageView *)<#avatarImv#> {
    if (!_<#avatarImv#>) {
        _<#avatarImv#> = [[UIImageView alloc] init];
        _<#avatarImv#>.contentMode = UIViewContentModeScaleAspectFill;
        _<#avatarImv#>.layer.cornerRadius = <#radiu#>;
        _<#avatarImv#>.layer.masksToBounds = YES;
        _<#avatarImv#>.userInteractionEnabled = YES;
        [_<#avatarImv#> addGestureRecognizer:[[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(avatarImvTap)]];
    }
    return _<#avatarImv#>;
}

### ppcell
- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier {
    if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier]) {
        self.selectionStyle = UITableViewCellSelectionStyleNone;
        self.backgroundColor = [UIColor clearColor];
        
        [self initViews];
    }
    return self;
}

- (void)initViews {
    [self.contentView addSubview:self.avatarImv];
    [self.avatarImv mas_makeConstraints:^(MASConstraintMaker *make) {
        make.left.equalTo(self.contentView).offset(15);
        make.right.equalTo(self.contentView).offset(-15);
        make.top.equalTo(self.contentView).offset(20);
        make.bottom.equalTo(self.contentView).offset(-20);
        make.centerY.equalTo(self.contentView);
    }];
}

### ppview
- (instancetype)initWithFrame:(CGRect)frame {
    if (self = [super initWithFrame:frame]) {
        self.backgroundColor = [UIColor clearColor];
        [self initViews];
    }
    return self;
}

- (void)initViews {
    
}

### NSLog  ppl
NSLog(@"%@", <#content#>);

### mark  ppm
#pragma mark - life cycle

#pragma mark - private method
- (void)p_initViews {
    
}

- (void)p_addObservers {

}

#pragma mark - public method

#pragma mark - network methods

#pragma mark - delegates

#pragma mark - event response

#pragma mark - setters

#pragma mark - getters

### tableView pptableview
#pragma mark - tableView delegate
- (CGFloat)tableView:(UITableView *)tableView heightForHeaderInSection:(NSInteger)section {
    return 0;
}

- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    return 0;
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    [tableView deselectRowAtIndexPath:indexPath animated:YES];
}

#pragma mark - tableView datasource
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return 1;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *cellIde = @"cellIde";
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:cellIde];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:cellIde];
    }
    return cell;
}

#pragma mark - getter
- (UITableView *)tableView {
    if (!_tableView) {
        _tableView = [[UITableView alloc] initWithFrame:CGRectZero style:UITableViewStylePlain];
        _tableView.delegate = self;
        _tableView.dataSource = self;
        _tableView.separatorStyle = UITableViewCellSeparatorStyleNone;
        _tableView.tableFooterView = [UIView new];
        _tableView.backgroundColor = [UIColor clearColor];
        _tableView.estimatedRowHeight = 0;
        _tableView.estimatedSectionHeaderHeight = 0;
        _tableView.estimatedSectionFooterHeight = 0;
        
        [_tableView registerClass:[<#cell#> class] forCellReuseIdentifier:@"<#cell#>"];
    }
    return _tableView;
}
