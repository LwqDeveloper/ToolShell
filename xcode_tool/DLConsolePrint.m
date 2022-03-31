//
//  DLConsolePrint.m
//  testPrint
//
//  Created by weiqiong.li on 2022/3/31.
//

#import "DLConsolePrint.h"

@implementation DLConsolePrint

@end

@implementation NSArray (DLPrint)

// 只需要在分类中,重写这个方法的实现,不需要导入分类文件就会生效
- (NSString *)descriptionWithLocale:(nullable id)locale indent:(NSUInteger)level
{
    // 定义用于拼接字符串的容器
    NSMutableString *stringM = [NSMutableString string];
    
    // 拼接开头
    [stringM appendString:@"(\n"];
    
    // 拼接中间的数组元素
    [self enumerateObjectsUsingBlock:^(id  _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
        
        [stringM appendFormat:@"\t%@,\n",obj];
        
    }];
    
    // 拼接结尾
    [stringM appendString:@")\n"];
    
    return stringM;
}

@end

@implementation NSDictionary (DLPrint)

// 只需要在分类中,重写这个方法的实现,不需要导入分类文件就会生效
- (NSString *)descriptionWithLocale:(nullable id)locale indent:(NSUInteger)level
{
    // 定义用于拼接字符串的容器
    NSMutableString *stringM = [NSMutableString string];
    
    // 拼接开头
    [stringM appendString:@"{\n"];
    
    // 遍历字典,拼接内容
    [self enumerateKeysAndObjectsUsingBlock:^(id  _Nonnull key, id  _Nonnull obj, BOOL * _Nonnull stop) {
        [stringM appendFormat:@"\t%@ = %@;\n",key,obj];
    }];
    
    // 拼接结尾
    [stringM appendString:@"}\n"];
    
    return stringM;
}

@end
